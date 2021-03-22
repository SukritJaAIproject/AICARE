import wave
import pyaudio
from PIL import ImageGrab
import numpy as np
import cv2
from moviepy.editor import *
from moviepy.audio.fx import all
import time

chunk=1024
format=pyaudio.paInt16
channels=2
rate=44100
wave_output_filename="output.wav"

p = pyaudio.PyAudio()
wf = wave.open (wave_output_filename, "wb")
wf.setnchannels (channels)
wf.setsampwidth (p.get_sample_size (format))
wf.setframerate (rate)
audio_record_flag=True

def callback (in_data, frame_count, time_info, status):
 wf.writeframes (in_data)
 if audio_record_flag:
  return (in_data, pyaudio.paContinue)
 else:
  return (in_data, pyaudio.paContinue)

stream=p.open (format=p.get_format_from_width (wf.getsampwidth ()), channels=wf.getnchannels (), rate=wf.getframerate (), input=True, stream_callback=callback)
image=ImageGrab.grab () #Get the current screen
width=image.size [0]
height=image.size [1]
print ("width:", width, "height:", height)
print ("image mode:", image.mode)
k=np.zeros ((width, height), np.uint8)

fourcc=cv2.VideoWriter_fourcc(* "xvid") #encoding format
video = cv2.VideoWriter("test.mp4", fourcc, 9.5, (width, height))

print ("video recording !!!!!")
stream.start_stream ()
print ("audio recording !!!!!")
record_count=0

while True:
 rgb=ImageGrab.grab()
 bgr=cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2BGR) #Convert to opencv's bgr format
 video.write(bgr)
 record_count +=1
 if (record_count>200):
  break
 print (record_count, time.time ())
audio_record_flag=False
while stream.is_active():
 time.sleep(1)
stream.stop_stream()
stream.close()
wf.close()
p.terminate()

print("audio recording done !!!!!")
video.release()
cv2.destroyAllWindows()

print("video recording done !!!!!")
print("video audio merge !!!!!")

audioclip=AudioFileClip("output.wav")
videoclip=VideoFileClip("test.mp4")
videoclip2=videoclip.set_audio(audioclip)
video=CompositeVideoClip([videoclip2])
video.write_videofile("test2.mp4", codec="mpeg4")