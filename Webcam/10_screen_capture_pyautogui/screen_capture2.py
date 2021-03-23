import cv2
import numpy as np
import pyautogui
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
SCREEN_SIZE = (screen_width, screen_height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    img = pyautogui.screenshot(region=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
    # region = {'top': 0, 'left': 0, 'width': 400, 'height': 300}
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()