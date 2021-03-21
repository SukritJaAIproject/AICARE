"""

Author: Ivanna
  
"""

import cv2
import numpy as np
import roslib
import rospy
import rospkg
from cv_bridge import CvBridge, CvBridgeError
from numpy import linalg as la
from sensor_msgs.msg import Image
import csv
import yaml
from sklearn.externals import joblib 


def scale_image(img, xfactor, yfactor):
    scaled = cv2.resize(img, None, fx=xfactor, fy=yfactor, interpolation=cv2.INTER_CUBIC)
    return scaled


def con_cvmat_from_image(image, encoding ="bgr8"):
    bridge = CvBridge()
    try:
        cv_mat = bridge.imgmsg_to_cv2(image, encoding)
     #   rospy.loginfo(cv_mat.shape)
        return cv_mat
    except CvBridgeError as e:
        rospy.logerr("", e)


def conv_image_from_cvmat(cv_mat, encoding = "bgr8"):
    rospy.loginfo(" --- converting cv mat to Image msg  --- ")
    bridge = CvBridge()
    try:
        rospy.loginfo("shape: %s, %s", cv_mat.shape[0], cv_mat.shape[1])
        msg = bridge.cv2_to_imgmsg(cv_mat,encoding)
        rospy.loginfo("%s %s", msg.width ,msg.height)
        return msg
    except CvBridgeError as e:
        rospy.logerr("error %s", e)


def load_configuration_from_file(path):
    with open(path) as file:
        return yaml.safe_load(file)
    


def translate_begin_of_coordinate(data, path_to_csv):
    data_new = np.copy(data)
    
    for row in data_new:
        x_neck = row[3]
        y_neck = row[4]

        for i in range(len(row)):
            if i > 0:
                if i % 2 == 1:
                    row[i] = row[i] - x_neck
                elif i % 2 == 0:
                    row[i] = row[i] - y_neck

    np.savetxt(path_to_csv, data_new, delimiter=';', fmt='%1.6f') 


def store_model(path, model):
    modelname =  path +  '.pkl'
    joblib.dump(model, modelname)


def save_report(path, classifier_name, report):
    with open(path, 'aw') as report_file:
        report_file.write('--- Classification report for %s ---' % classifier_name)
        report_file.write('\n')
        report_file.write(report)

def print_prediction_result(result=[], classes=[]):
    assert len(classes)==len(result)
    for (conf, cl) in zip(result, classes):
        print(cl+': {0:.4g}'.format(conf))
