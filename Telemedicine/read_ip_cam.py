import numpy as np
import cv2

cap1 = cv2.VideoCapture("rtsp://admin:abc12345678@192.168.22.24:554/cam/realmonitor?channel=1&subtype=1 - Sub stream")
cap2 = cv2.VideoCapture("rtsp://admin:abc12345678@192.168.22.26:554/cam/realmonitor?channel=1&subtype=1 - Sub stream")
while (True):
    ret1 , frame1 = cap1.read()
    ret2 , frame2 = cap2.read()
    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
