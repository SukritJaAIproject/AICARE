import numpy as np
import cv2
import csv
import pandas as pd
import os
from datetime import datetime

################### pyfeat #########################
from feat import Detector
from feat.tests.utils import get_test_data_path
from PIL import Image
import matplotlib.pyplot as plt
from feat.utils import read_feat

face_model = "retinaface"
landmark_model = "mobilenet"
au_model = "rf"
emotion_model = "resmasknet"
detector = Detector(face_model = face_model, landmark_model = landmark_model, au_model = au_model, emotion_model = emotion_model)


cap = cv2.VideoCapture('http://192.168.1.39:56000/mjpeg')

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255,255,255)
lineType = 2

while(True):

    ret, frame = cap.read()
    cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\001.jpg', frame)

    test_image = r"C:\Users\sukri\Desktop\input\img\001.jpg"
    image_prediction = detector.detect_image(test_image)
    print(image_prediction)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()