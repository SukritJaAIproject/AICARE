import numpy as np
import cv2
from datetime import datetime
import os

path = 'vdo'
# filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
filename ="defaultvdo.avi"

# local webcam
# cap = cv2.VideoCapture(0)

# local logitech
cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)


# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640,480))

while(cap.isOpened()):
   ret, frame = cap.read()
   if ret==True:
       # frame = cv2.flip(frame,0)

       # write the flipped frame
       # out.write(frame)
       videoWriter.write(frame)

       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
   else:
       break

cap.release() # out.release()
videoWriter.release()
cv2.destroyAllWindows()