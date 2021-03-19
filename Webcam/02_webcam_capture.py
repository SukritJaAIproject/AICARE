import cv2
import os
import time
from datetime import datetime

print(cv2.getBuildInformation())

time_sum = 0
frames = 0

capture = cv2.VideoCapture()
capture.open(1 + cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
capture.set(cv2.CAP_PROP_FOURCC, fourcc)
capture.set(cv2.CAP_PROP_FPS, 30)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

while(1):
    before_timer = time.perf_counter()
    ret, frame = capture.read()
    if frame is None:
        print("Frame is empty")
        break
    else:
        # cv2.imshow('VIDEO', frame)

        path = 'img'
        filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".png"
        # filename = "image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")) + ".png"
        cv2.imwrite(os.path.join(path, filename), frame)

        after_timer = time.perf_counter() - before_timer
        time_sum += after_timer
        frames += 1
        if frames % 30 == 0:
            print("{} per second".format(frames/time_sum))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# After the loop release the cap object
capture.release()
# Destroy all the windows
cv2.destroyAllWindows()

#######https://www.reddit.com/r/computervision/comments/dgdjcs/logitech_brio_with_opencv_videocapture/########
# import cv2
# import time
#
# cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
#
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# cap.set(cv2.CAP_PROP_FOURCC, fourcc)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# t0 = time.time()
# framesComputed = 0
#
# while True:
#    frame, ret = cap.read()
#    framesComputed += 1
#
#    if time.time() - t0 > 1.:
#        print(framesComputed, ret.shape)
#
#    framesComputed = 0
#    t0 = time.time()
#
#    cv2.imshow('VIDEO', frame)
#    cv2.waitKey(1)

########################################
# import cv2
#
# cap = cv2.VideoCapture(1)
#
# while True:
#     _, frame = cap.read()
#     cv2.imshow('frame', frame)
#     cv2.waitKey(1)

################https://answers.opencv.org/question/216074/4k-videocapture-very-slow-on-windows-compared-to-ms-camera-app/######################
# okay