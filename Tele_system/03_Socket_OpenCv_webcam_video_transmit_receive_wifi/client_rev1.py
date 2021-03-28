# lets make the client code
import socket,cv2, pickle,struct
import time
import os
from datetime import datetime
import numpy as np
import pandas as pd

# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.1.39' # paste your server ip address here
port = 9999
client_socket.connect((host_ip,port)) # a tuple
data = b""
payload_size = struct.calcsize("Q")

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (640, 480))
font = cv2.FONT_HERSHEY_SIMPLEX
lineType = 2

prev_frame_time = 0
new_frame_time = 0

while True:
	while len(data) < payload_size:
		packet = client_socket.recv(4*1024) # 4K
		if not packet: break
		data+=packet
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q",packed_msg_size)[0]
	
	while len(data) < msg_size:
		data += client_socket.recv(4*1024)
	frame_data = data[:msg_size]
	data  = data[msg_size:]
	frame = pickle.loads(frame_data)

	cv2.imwrite(r'C:\Users\sukri\Desktop\AICARES\AICARE\Tele_system\03_Socket_OpenCv_webcam_video_transmit_receive_wifi\img\001.jpg', frame)
	os.system(r'cmd /c "C:\Users\sukri\Desktop\OpenFace_2.2.0_win_x64\FaceLandmarkImg.exe -f "C:\Users\sukri\Desktop\AICARES\AICARE\Tele_system\03_Socket_OpenCv_webcam_video_transmit_receive_wifi\img\001.jpg" -out_dir C:\Users\sukri\Desktop\openface_result -of reco -aus"')
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

	new_frame_time = time.time()
	fps = 1 / (new_frame_time - prev_frame_time)
	prev_frame_time = new_frame_time
	fps = round(fps, 2)
	fps = str(fps)
	print(fps)

	cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

	cv2.imshow("RECEIVING VIDEO",frame)
	cv2.imshow("img", img1)

	key = cv2.waitKey(1) & 0xFF
	if key  == ord('q'):
		break
client_socket.close()
