import cv2
import pandas as pd
import matplotlib.pyplot as plt

while(True):

    df = pd.read_csv(r"C:\Users\sukri\Desktop\AICARES\AICARE\Facial_Action_Coding_System_FACS\03_openface\reco_au.csv")

    if df.shape[0] > 100:
        df = df.iloc[-100:,:]
        df.to_csv('reco_au.csv', index=False)

    lines = df.plot.line()
    plt.savefig('lines.png')
    img_lines = cv2.imread('lines.png')
    cv2.imshow('img_lines', img_lines)
    plt.close('all')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()