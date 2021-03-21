import cv2
import zmq
import base64
import numpy as np
from datetime import datetime
import os

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640, 480))

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        print(source.shape)
        videoWriter.write(source)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.des
