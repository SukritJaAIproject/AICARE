import argparse
import cv2
import numpy as np
import zmq
from constants import PORT
from utils import string_to_image
from datetime import datetime
import os
import pandas as pd
import time

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
lineType = 2

class StreamViewer:
    def __init__(self, port=PORT):
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.SUB)
        self.footage_socket.bind('tcp://*:' + port)
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
        self.current_frame = None
        self.keep_running = True
        self.prev_frame_time = 0
        self.new_frame_time = 0

    def receive_stream(self, display=True):
        self.keep_running = True
        while self.footage_socket and self.keep_running:
            try:
                frame = self.footage_socket.recv_string()
                self.current_frame = string_to_image(frame)

                if display:
                    print(self.current_frame.shape)
                    # videoWriter.write(self.current_frame)

                    cv2.imwrite(r'C:\Users\sukri\Desktop\AICARES\AICARE\Tele_system\01_SmoothStream\img\001.jpg', self.current_frame)
                    os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\AICARES\AICARE\Tele_system\01_SmoothStream\img\001.jpg" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
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

                    self.new_frame_time = time.time()
                    fps = 1 / (self.new_frame_time - self.prev_frame_time)
                    self.prev_frame_time = self.new_frame_time
                    fps = round(fps,2)
                    fps = str(fps)
                    print(fps)

                    cv2.putText(self.current_frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

                    cv2.imshow("Stream", self.current_frame)
                    cv2.imshow("img", img1)
                    cv2.waitKey(1)

            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                break
        print("Streaming Stopped!")

    def stop(self):
        self.keep_running = False

def main():
    port = PORT
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port',help='The port which you want the Streaming Viewer to use, default'' is ' + PORT, required=False)

    args = parser.parse_args()
    if args.port:
        port = args.port

    stream_viewer = StreamViewer(port)
    stream_viewer.receive_stream()

if __name__ == '__main__':
    main()
