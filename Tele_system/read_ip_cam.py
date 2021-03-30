import numpy as np
import cv2
import csv
import pandas as pd
import os
from import_csv import *
from datetime import datetime

cap = cv2.VideoCapture('http://192.168.1.39:56000/mjpeg')
# cap = cv2.VideoCapture(0)


################### record vdo #####################################
# path = 'vdo'
# path = r'C:\Users\sukri\Desktop\input\vdo'
# filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
# filename = "default.avi"
# cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640,480))

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255,255,255)
lineType = 2

# i = 1
while(True):

    ret, frame = cap.read()
    print(frame.shape)
    cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\001.jpg', frame)
    # cv2.imwrite(r'C:\Users\sukri\Desktop\input\img\00'+str(i)+'.jpg', frame)

    # record vdo
    # videoWriter.write(frame)

    # data = import_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv')
    # first_row = data[0]
    # last_row = data[-1]
    # first_row = [i.strip() for i in first_row]
    # last_row = [float(i) for i in last_row]
    # df = pd.DataFrame(last_row).T
    # df.columns = first_row

    img1 = np.zeros((512, 512, 3), np.uint8)
    df = pd.read_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv')
    df.columns = [i.strip() for i in df.columns]
    print(df.shape)

    # if df.shape[0] > 100:
    #     df = df.iloc[-100:,:]
    #     df.to_csv(r'C:\Users\sukri\Desktop\openface_result\reco.csv', index=False)

    offset = 35
    x, y = 50, 50
    AUr = df.columns[5:17]
    for idx, lbl in enumerate(AUr):
        # cv2.putText(img1, str(df.columns[idx]) + ' :' + str(df[[lbl]].values[0][0]), (10,500), font, fontScale,fontColor, lineType)
        cv2.putText(img1, str(df.columns[idx+5]) + ' :' + str(df[[lbl]].values[0][0]), (x,y+offset*idx), font, fontScale,
                    fontColor, lineType)

    cv2.imshow('frame',frame)
    cv2.imshow("img", img1)

    #vdo
    # os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -device 1 -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
    os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\input\img\001.jpg" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
    # os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\input\img\001.jpg" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
    # os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -f "C:\Users\sukri\PycharmProjects\testssss\vdo\default.avi" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
    # os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FeatureExtraction.exe -f "C:\Users\sukri\PycharmProjects\testssss\vdo\default.avi" "')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # i+=1

cap.release()
cv2.destroyAllWindows()