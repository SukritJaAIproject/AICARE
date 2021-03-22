import socket, cv2, pickle, struct
import imutils  # pip install imutils
import threading
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
videoWriter = cv2.VideoWriter(os.path.join(path, filename), fourcc, 30.0, (320, 240))

global frame
frame = None

def start_video_stream():
   global frame
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host_ip = '192.168.1.44'  # Here provide Drone IP
   port = 9999
   client_socket.connect((host_ip, port))
   data = b""
   payload_size = struct.calcsize("Q")
   while True:
       while len(data) < payload_size:
           packet = client_socket.recv(4 * 1024)
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
       print(frame.shape)
       videoWriter.write(frame)
       cv2.imshow("RECEIVING VIDEO FROM DRONE", frame)
       key = cv2.waitKey(1) & 0xFF
       print(data)
       if key == ord('q'):
           break
   client_socket.close()

thread = threading.Thread(target=start_video_stream, args=())
thread.start()

def serve_client(addr, client_socket):
   global frame
   try:
       print('CLIENT {} CONNECTED!'.format(addr))
       if client_socket:
           while True:
               a = pickle.dumps(frame)
               message = struct.pack("Q", len(a)) + a
               client_socket.sendall(message)

   except Exception as e:
       print(f"CLINET {addr} DISCONNECTED")
       pass

while True:
   client_socket, addr = server_socket.accept()
   print(addr)
   thread = threading.Thread(target=serve_client, args=(addr, client_socket))
   thread.start()
   print("TOTAL CLIENTS ", threading.activeCount() - 2)  # edited here because one thread is already started before
