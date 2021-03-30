import cv2
import pandas as pd
import matplotlib.pyplot as plt

while(True):

    df = pd.read_csv("au_output.csv")

    if df.shape[0] > 100:
        df = df.iloc[-100:,:]
        df.to_csv('au_output.csv', index=False)

    lines = df.plot.line()
    plt.savefig('lines.png')
    img_lines = cv2.imread('lines.png')
    cv2.imshow('img_lines', img_lines)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()