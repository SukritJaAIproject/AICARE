# AICARE

*	##	01 Facial_Keypoint
		ใน folder นี้จะเป็นการสกัด Facial landmark ด้วยโมเดลต่างๆ เช่น dlib, XceptionNetResNet18,
		Openpose, Conv2D, stasm, keras_Con2D, และ mediapipe
		โดยในส่วนของ openpose ก็จะถูกแปลงไปอยู่ในหลายๆ library เช่น 
		Tensorflow2, Chainer_model, original openpose,และ readNetFromCaffe
*	##	02 Facial_Action_Coding_System_FACS
		ใน folder นี้จะเป็นการสกัด Action Unit (AU) ด้วยโมเดลต่างๆ เช่น openface, Action_Units_Heatmaps, และ FER
*	##	03 Integrated_part
		ใน folder นี้จะเป็นการนำ Facial landmark และ Action Unit (AU) หรือ features อื่นๆ เช่น  Hog, raw image เป็นต้น 
		มาเข้า classification model เพื่อ classify ว่า ณ ขณะนี้คนไข้มีการแสดงออกทางอารมณ์อย่างไร
*	##	04 Eye_movement
		ใน folder นี้การนำ Facial landmark มาวิเคราะห์การแสดงออกทางดวงตา มองขึ้นด้านบน-ล่าง, มองไปทางซ้าย-ขวา
*	##	05 Upper_Body_Movement 
		ใน folder นี้จะเป็นการวิเคราะห์การเคลื่อนไหวของร่างกายส่วนบน เช่น มีการขยับของศีรษะลดลง, มีการแสดงออกผ่านทางมือลดลง เป็นต้น
*	##	06 Tele_system
		ใน folder นี้จะเป็นการทำสอบระบบ Tele system
*	##	07 Webcam
		ใน folder นี้จะเป็นการบันทึกข้อมูลด้วยกล้อง webcam และ sound recorder
