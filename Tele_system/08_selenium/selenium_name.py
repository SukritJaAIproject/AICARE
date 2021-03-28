# importing webdriver from selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
import os
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://192.168.1.39:5000/"
# driver = webdriver.Chrome()

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
lineType = 2

prev_frame_time = 0
new_frame_time = 0



while(1):

    driver.get(url)
    driver.save_screenshot("image.png")
    # image = Image.open("image.png")
    img = cv2.imread('image.png')

    os.system(
        r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\AICARES\AICARE\Tele_system\08_selenium\image.png" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
    img1 = np.zeros((640, 480, 3), np.uint8)
    df = pd.read_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv')
    df.columns = [i.strip() for i in df.columns]

    offset = 20
    x, y = 50, 50
    AUr = df.columns[2:17]
    for idx, lbl in enumerate(AUr):
        cv2.putText(img1, str(df.columns[idx + 2]) + ' :' + str(df[[lbl]].values[0][0]),
                    (x, y + offset * idx), font, 0.5,
                    (100, 255, 0), lineType)

    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = round(fps, 2)
    fps = str(fps)
    print(fps)

    cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)


    cv2.imshow('image', img)
    cv2.imshow("img", img1)
    # driver.close()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

driver.close()