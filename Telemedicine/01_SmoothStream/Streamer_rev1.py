import argparse
import cv2
import numpy as np
import zmq
from constants import PORT
from utils import string_to_image

class StreamViewer:
   def __init__(self, port=PORT):
       context = zmq.Context()
       self.footage_socket = context.socket(zmq.SUB)
       self.footage_socket.bind('tcp://*:' + port)
       self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
       self.current_frame = None
       self.keep_running = True

   def receive_stream(self, display=True):
       self.keep_running = True
       while self.footage_socket and self.keep_running:
           try:
               frame = self.footage_socket.recv_string()
               self.current_frame = string_to_image(frame)

               if display:
                   cv2.imshow("Stream", self.current_frame)
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
   parser.add_argument('-p', '--port',
                       help='The port which you want the Streaming Viewer to use, default'
                            ' is ' + PORT, required=False)

   args = parser.parse_args()
   if args.port:
       port = args.port

   stream_viewer = StreamViewer(port)
   stream_viewer.receive_stream()


if __name__ == '__main__':
   main()
