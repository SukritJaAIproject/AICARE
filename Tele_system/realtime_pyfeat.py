import numpy as np
import cv2
import csv
import pandas as pd
import os
from datetime import datetime
import time

################### pyfeat #########################
from feat import Detector
from feat.tests.utils import get_test_data_path
from PIL import Image
import matplotlib.pyplot as plt
from feat.utils import read_feat

################### calculate FPS #########################
prev_frame_time = 0
new_frame_time = 0

face_model = "retinaface"
landmark_model = "mobilenet"
au_model = "rf"
emotion_model = "resmasknet"
detector = Detector(face_model = face_model, landmark_model = landmark_model, au_model = au_model, emotion_model = emotion_model)

cap = cv2.VideoCapture('http://192.168.1.39:56000/mjpeg')
# cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255,255,255)
lineType = 2

while(True):

    ret, frame = cap.read()
    new_frame_time = time.time()

    cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\001.png', frame)
    test_image = r"C:\Users\sukri\Desktop\input\img\001.png"
    image_prediction = detector.detect_image(test_image)
    print(image_prediction)

    image_prediction.plot_detections()
    # pics = image_prediction.plot_detections(draw_landmarks=False, draw_facelines=False, muscle=False)
    # pics = image_prediction.plot_detections(draw_landmarks=True, draw_facelines=True, muscle=True)

    img = cv2.imread('fooss.png')
    cv2.imshow('image', img)
    plt.close('all')

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = round(fps,2)
    fps = str(fps)
    print(fps)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()