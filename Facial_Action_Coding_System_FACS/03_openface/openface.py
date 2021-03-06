import numpy as np
import cv2
import csv
import pandas as pd
import os
# from import_csv import *

import glob, os

from PIL._imaging import display
from feat.tests.utils import get_test_data_path
from feat.utils import read_openface


cap = cv2.VideoCapture('http://192.168.1.39:56000/mjpeg')
# cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255,255,255)
lineType = 2
df_au = pd.read_csv('reco_au.csv')

# i = 1
while(True):

    # print('all() =', detections.head())
    # print('landmark() = ', detections.landmark().head())
    # print('aus() =', detections.aus().head())

    ret, frame = cap.read()
    print(frame.shape)
    cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\001.jpg', frame)
    # cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\00'+str(i)+'.jpg', frame)


    # data = import_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv')
    # first_row = data[0]
    # last_row = data[-1]
    # first_row = [i.strip() for i in first_row]
    # last_row = [float(i) for i in last_row]
    # df = pd.DataFrame(last_row).T
    # df.columns = first_row

    # img1 = np.zeros((512, 512, 3), np.uint8)
    # df = pd.read_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv')
    # df.columns = [i.strip() for i in df.columns]
    # print(df.shape)

    # if df.shape[0] > 100:
    #     df = df.iloc[-100:,:]
    #     df.to_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv', index=False)

    # offset = 35
    # x, y = 50, 50
    # AUr = df.columns[5:17]
    # for idx, lbl in enumerate(AUr):
    #     # cv2.putText(img1, str(df.columns[idx]) + ' :' + str(df[[lbl]].values[0][0]), (10,500), font, fontScale,fontColor, lineType)
    #     cv2.putText(img1, str(df.columns[idx+5]) + ' :' + str(df[[lbl]].values[0][0]), (x,y+offset*idx), font, fontScale,
    #                 fontColor, lineType)

    cv2.imshow('frame',frame)
    # cv2.imshow("img", img1)

    os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\input\img\001.jpg" -of reco"')
    openface_file = r'C:\Users\sukri\Desktop\AICARES\AICARE\Facial_Action_Coding_System_FACS\03_openface\processed\reco.csv'
    detections = read_openface(openface_file)
    df_au = df_au.append(detections.aus())
    df_au.to_csv('reco_au.csv', index=False)
    print(df_au.shape)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # i+=1

cap.release()
cv2.destroyAllWindows()







# vdo
# os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -device 1 -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
# os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\input\img\001.jpg" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
# os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -f "C:\Users\sukri\PycharmProjects\testssss\vdo\default.avi" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
# os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -f "C:\Users\sukri\PycharmProjects\testssss\vdo\default.avi" "')
