import socket, cv2, pickle, struct
import imutils
import threading
import pyshine as ps  # pip install pyshine
import cv2
from datetime import datetime
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)

path = 'vdo'
filename = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (380, 285))

def show_client(addr, client_socket):
   try:
       print('CLIENT {} CONNECTED!'.format(addr))
       if client_socket:  # if a client socket exists
           data = b""
           payload_size = struct.calcsize("Q")
           while True:
               while len(data) < payload_size:
                   packet = client_socket.recv(4 * 1024)  # 4K
                   if not packet: break
                   data += packet
               packed_msg_size = data[:payload_size]
               data = data[payload_size:]
               msg_size = struct.unpack("Q", packed_msg_size)[0]

               while len(data) < msg_size:
                   data += client_socket.recv(4 * 1024)
               frame_data = data[:msg_size]
               data = data[msg_size:]
               frame = pickle.loads(frame_data)
               text = f"CLIENT: {addr}"
               frame = ps.putBText(frame, text, 10, 10, vspace=10, hspace=1, font_scale=0.7,
                                   background_RGB=(255, 0, 0), text_RGB=(255, 250, 250))
               print(frame.shape)
               videoWriter.write(frame)
               cv2.imshow(f"FROM {addr}", frame)
               key = cv2.waitKey(1) & 0xFF
               if key == ord('q'):
                   break
           client_socket.close()
   except Exception as e:
       print(f"CLINET {addr} DISCONNECTED")
       pass

while True:
   client_socket, addr = server_socket.accept()
   thread = threading.Thread(target=show_client, args=(addr, client_socket))
   thread.start()
   print("TOTAL CLIENTS ", threading.activeCount() - 1)
