##	01_images_model.ipynb
	ใช้ input เป็นรูป โมเดลเป็น Conv2D

##	02_Facial_expressions_model
	- 02_Convert_fer2013_to_img_landmarks_HOG_Window.ipynb
		เป็นการแปลง fer2013 dataset ให้เป็น features -> img, facial landmarks,HOG, และ Window
		
	- 02_Facial_expressions_model.ipynb
		เป็น code ที่ยังไม่ได้ clean
		
	- 02_Train_Facial_expressions_model_Facelandmarks_HOG_sliding_window.ipynb
		เป็น train model ที่มี input เป็น original image, Facelandmarks, HOG, และ sliding_window
		
	- 02_Train_Facial_expressions_model_use_hog_and_landmarks.ipynb
		เป็น train model ที่มี input เป็น original image, Facelandmarks, และ HOG
		
	- 02_Train_Facial_expressions_model_use_landmarks.ipynb
		เป็น train model ที่มี input เป็น original image และ Facelandmarks
	
	- 02_predictive_use_hog_and_landmarks.ipynb
		เป็น code ที่ใช้ในการ deploy สำหรับ input ที่เป็น hog และ landmark
	
	- 02_predictive_use_hog_sliding_window_and_landmarks.ipynb
		เป็น code ที่ใช้ในการ deploy สำหรับ input ที่เป็น hog, sliding_window และ landmark
	
	- 02_predictive_use_landmarks.ipynb
		เป็น code ที่ใช้ในการ deploy สำหรับ input ที่เป็น landmark

##	03_Facial_recognition_fastai.ipynb