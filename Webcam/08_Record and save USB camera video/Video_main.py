import cv2
import os
import datetime

def read_usb_capture():
    # Select the number of the camera
    cap = cv2.VideoCapture(1)
    # Add this sentence is a pop-up window that can be dragged with the mouse
    cv2.namedWindow('real_img', cv2.WINDOW_NORMAL)

    # .mp4 format, 25 is FPS frame rate, (640,480) is size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('temp.mp4', fourcc, 25, (640, 480))

    while(cap.isOpened()):
        # Read the picture of the camera
        ret, frame = cap.read()

        # Perform write operation
        out.write(frame)
        # Real picture
        cv2.imshow('real_img', frame)
        # Press'esc' to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # Release screen
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    os.system("start cmd_.vbe") #Start recording
    read_usb_capture() # Start camera
    name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # Current time
    os.system("ffmpeg -i temp.mp4 -i temp.wav -strict -2 -f mp4 " + name + ".mp4")  # Use ffmpe to merge
    os.remove('temp.mp4') # Delete the intermediate video file
    os.remove("temp.wav") # Delete intermediate audio files

