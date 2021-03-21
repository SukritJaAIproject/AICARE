import cv2
import numpy as np
from numpy import linalg as la
import argparse
from time import time
from utility import load_configuration_from_file, store_model, save_report, print_prediction_result
from collections import Counter

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.tree.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.externals import joblib
from imblearn.over_sampling import SMOTE
import os


parser = argparse.ArgumentParser(
        description='This script is used for human gesture estimation ')
parser.add_argument('--train', help='Start training the models if this argument is set to true')
parser.add_argument('--pred', help='Run prediction if the argument is set to true')
parser.add_argument('--features', default='sample_features.npz', help='Openpose features stored in numpy format')
parser.add_argument('--image', default='sample_image.png', help='Input image')
parser.add_argument('--model', default='random_forest.pkl',  help='Specify path to the model used for prediction')
parser.add_argument('--pretrained', default='true',  help='Use pretrained models for prediction')

args = parser.parse_args()

HOMEDIR = os. environ['HOME']
CONFIG_FILE = 'config/training_data_description.yaml'

training_data = None
best_estimator_report = None
classification_report = None
path_to_tr_data = None
header = None
model_config = None
persist_models_dir = None
feature_number = 120


def init():
	global training_data, best_estimator_report, classification_report, header, persist_models_dir, path_to_tr_data, model_config
	config = load_configuration_from_file(CONFIG_FILE)
	path_to_tr_data = HOMEDIR + config['data_file_config']['path_to_trainig_data']
	model_config = config['model_tuning_parameters']
	best_estimator_report = HOMEDIR + config['data_file_config']['best_estimator_search_report']
	classification_report = HOMEDIR + config['data_file_config']['classification_report']
	persist_models_dir = HOMEDIR + config['data_file_config']['persist_models_dir']
	header = config['data_file_config']['header']
	feature_number = config['data_file_config']['feature_number']


def preapere_data_for_training():
	config = load_configuration_from_file(CONFIG_FILE)
	smote = SMOTE(ratio='all')

	training_data = np.genfromtxt(path_to_tr_data, delimiter=';')
	assert training_data.shape[0]>0 and training_data.shape[1]>0
	observations = training_data[:, 1:]
	target = training_data[:,:1].ravel()
	sm_observations, sm_target = smote.fit_sample(observations, target)
	classifiers = init_classifiers(model_config, sm_observations, sm_target)
   
	for cl_name, classifier in classifiers.items():
		train_and_store_models(sm_observations, sm_target, classifier, cl_name)



def search_best_param_for_model(name, classifier, tuning_parameters, observations, targets, _test_size=0.3, _random_state=0, save_report = True):

	if tuning_parameters != None and len(tuning_parameters) > 0:
		X_train, X_test, y_train, y_test = train_test_split(observations, targets, test_size=_test_size, random_state=_random_state)
		estimator_to_score = {}
		scores = ['precision_macro', 'recall_macro', 'accuracy']
		
		for score in scores: 
			print("# Tuning hyper-parameters for %s" % score)
			
			clf = GridSearchCV(classifier, tuning_parameters,  verbose=2, cv=10, scoring=score)
			clf.fit(X_train, y_train)
			estimator_to_score[clf.best_score_] = clf.best_estimator_
			y_true, y_pred = y_test, clf.predict(X_test)
			report = classification_report(y_true, y_pred)

			print(' Best estimator set found on development set: %s' % clf.best_estimator_)
			
			if save_report:
				with open(best_estimator_report, 'a') as report_file:
					report_file.write('Classifier ' + name + '\n')
					report_file.write('Tuning hyper-parameters for %s' % score)
					report_file.write('\nBest scores: ')
					report_file.write(str(clf.best_score_))
					report_file.write('\nReport: \n')
					report_file.write(report)

		scores_sorted =  sorted(estimator_to_score, reverse=True)
		return estimator_to_score[scores_sorted[0]]



def adjust_adaboost_param(tuning_param):
	if tuning_param['base_estimator_name'] == 'DecisionTreeClassifier':
		tuning_param['base_estimator'] = []
		
		for max_feature in tuning_param['base_estimator_max_features']:
			tuning_param['base_estimator'].append(DecisionTreeClassifier(max_features = max_feature))

		tuning_param.pop('base_estimator_name')
		tuning_param.pop('base_estimator_max_features')
		return tuning_param



def train_and_store_models(X, y, classifier, name, persist_model = True, store_report = True):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
	print (' ---- Training using %s --- ' % name)
	cls = classifier
 
	model = cls.fit(X_train, y_train)
	y_true, y_predicted = y_test, model.predict(X_test)
	report = classification_report(y_true, y_predicted)
	print(report)

	if store_report:
		save_report(HOMEDIR + classification_report, name,  report)

	if persist_model:
		store_model(HOMEDIR + persist_models_dir + name, model)
		
	


def init_classifiers(model_condig, observations, target):
	classifiers = {}
	
	for key in model_condig.keys():
		print 'Initializing classigier ',  key
		if key == 'svm':
			best_estimator = search_best_param_for_model(key, SVC(), model_condig[key], observations, target)
			classifiers[key] = best_estimator

		if key == 'decision_tree':
			best_estimator = search_best_param_for_model(key, DecisionTreeClassifier(), model_condig[key], observations, target)
			classifiers[key] = best_estimator

		if key == 'random_forest':
			best_estimator = search_best_param_for_model(key, RandomForestClassifier(), model_condig[key], observations, target)
			classifiers[key] = best_estimator

		if key == 'adaboost':
			best_estimator = search_best_param_for_model(key, AdaBoostClassifier(base_estimator=DecisionTreeClassifier()), adjust_adaboost_param(model_condig[key]), observations, target)
			classifiers[key] = best_estimator

	return classifiers



def load_model_and_predict():
	print('Predicting using %s classifier' % args.model)
	if args.pretrained == 'true':
		model = './models/gestrec_pretrained/' + args.model
	else:
		model = HOMEDIR + persist_models_dir + args.model
	clf = joblib.load(model)
	
	features = np.load(args.features)['features']
	assert features.reshape(1, -1).shape[1] == feature_number, 'Expected 120 features'
	result = clf.predict_proba(features.reshape(1, -1))
	print_prediction_result(result[0], header[1:])
	mat = cv2.imread(args.image)
	text_as_str = []
	text_as_str.append('waving_right:{0:.4g}'.format(result[0][0]))
	text_as_str.append('waving_left:{0:.4g}'.format(result[0][1]))
	text_as_str.append('pointing_right:{0:.4g}'.format(result[0][2]))
	text_as_str.append('pointing_left:{0:.4g}'.format(result[0][3]))
	text_as_str.append('stop:{0:.4g}'.format(result[0][4]))
                    
	font = cv2.FONT_HERSHEY_SIMPLEX
	y = 20 
	for t in text_as_str:
		y = y + 20
		cv2.putText(mat, t, (10, y), font, 0.6, (0, 255, 0), 1, cv2.LINE_AA)
	cv2.imwrite('sample_classified.png', mat)

    

if __name__ == "__main__":
	
	if args.train == 'true':
		print('########## Starting training ##########')
		init()
		preapere_data_for_training()
	elif args.pred == 'true':
		print('########## Predicting ##########')
		init()
		load_model_and_predict()
	else:
		raise ValueError('Specify operation')
