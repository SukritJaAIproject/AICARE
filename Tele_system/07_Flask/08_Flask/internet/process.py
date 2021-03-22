from flask import Flask, render_template, request,Response
import cv2,imutils,time
import pyshine as ps
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

def changeBrightness(img,value):
	""" This function will take an image (img) and the brightness
		value. It will perform the brightness change using OpenCv
		and after split, will merge the img and return it.
	"""
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	h,s,v = cv2.split(hsv)
	lim = 255 - value
	v[v>lim] = 255
	v[v<=lim] += value
	final_hsv = cv2.merge((h,s,v))
	img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
	return img

def changeBlur(img,value):
	""" This function will take the img image and blur values as inputs.
		After perform blur operation using opencv function, it returns
		the image img.
	"""
	kernel_size = (value+1,value+1) # +1 is to avoid 0
	img = cv2.blur(img,kernel_size)
	return img

def pyshine_process(params):
	print("Parameters:",params)
	"""Video streaming generator function."""
	CAMERA=False
	if CAMERA:
		cap = cv2.VideoCapture(0)
	else:
		cap = cv2.VideoCapture('videos/mario.mp4')
	print('FUNCTION DONE')
	# Read until video is completed
	fps=0
	st=0
	frames_to_count=20
	cnt=0


	while(cap.isOpened()):

		ret, img = cap.read()
		brightness_value_now = int(params['brightness'])
		blur_value_now = int(params['blur'])
		img = changeBrightness(img,brightness_value_now)
		img = changeBlur(img,blur_value_now)
		if ret == True:

			if cnt == frames_to_count:
				try: # To avoid divide by 0 we put it in try except

					fps = round(frames_to_count/(time.time()-st))
					st = time.time()
					cnt=0
				except:
					pass

			cnt+=1

			img = imutils.resize(img, width=640)

			text  =  'FPS: '+str(fps)
			img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,background_RGB=(10,20,222))
			text = str(time.strftime("%d %b %Y %H.%M.%S %p"))
			img = ps.putBText(img,text,text_offset_x=190,text_offset_y=30,background_RGB=(228,20,222))
			text  =  f"Brightness: {brightness_value_now}"
			img = ps.putBText(img,text,text_offset_x=20,text_offset_y=300,background_RGB=(20,210,4))
			text  =  f'Blur: {blur_value_now}'
			img = ps.putBText(img,text,text_offset_x=490,text_offset_y=300,background_RGB=(210,20,4))
			frame = cv2.imencode('.JPEG', img,[cv2.IMWRITE_JPEG_QUALITY,20])[1].tobytes()
			time.sleep(0.016)
			yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
		else:
			break


@app.route('/res',methods = ['POST','GET'])
def res():
	global result
	if request.method == 'POST':
		result = request.form.to_dict()
		return render_template("results.html",result = result)

@app.route('/results')
def video_feed():
	global result
	params= result
	return Response(pyshine_process(params),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True,threaded=True)