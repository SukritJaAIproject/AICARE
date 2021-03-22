# canny_filter.py
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from datetime import datetime
import os

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640, 480))


class VideoTransformer(VideoTransformerBase):
   def transform(self, frame):
       img = frame.to_ndarray(format="bgr24")

       img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
       print(img.shape)
       videoWriter.write(img)
       # cv2.imshow("RECEIVING VIDEO FROM CACHE SERVER", img)
       return img

webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)