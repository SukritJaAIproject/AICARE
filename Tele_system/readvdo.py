# Find the file you want to process.
from feat.tests.utils import get_test_data_path
from feat import Detector

face_model = "retinaface"
landmark_model = "mobilenet"
au_model = "rf"
emotion_model = "resmasknet"
detector = Detector(face_model = face_model, landmark_model = landmark_model, au_model = au_model, emotion_model = emotion_model)

import os, glob
test_data_dir = get_test_data_path()
test_video = r"C:\Users\sukri\Desktop\AICARES\AICARE\Webcam\vdo\defaultvdo.avi"

# Show video
# from IPython.display import Video
# Video(test_video, embed=True)

# Show video
video_prediction = detector.detect_video(test_video, skip_frames=24)
print(video_prediction.head())

