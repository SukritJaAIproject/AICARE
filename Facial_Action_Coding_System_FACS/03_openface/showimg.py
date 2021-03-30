import cv2
import pandas as pd
import matplotlib.pyplot as plt
from feat.utils import read_openface

while(True):

    openface_file = r'C:\Users\sukri\Desktop\AICARES\AICARE\Facial_Action_Coding_System_FACS\03_openface\processed\reco.csv'
    detections = read_openface(openface_file)

    ax = detections.aus().T.plot(kind="barh")
    ax.invert_yaxis()
    ax.get_legend().remove()
    ax.set(xlim=[0, 1.1], title="Action Units")
    plt.savefig('fooss.png')
    img = cv2.imread('fooss.png')
    cv2.imshow('image', img)
    plt.close('all')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()