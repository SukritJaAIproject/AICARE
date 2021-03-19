OPENPOSE STATE OF THE ART
	อะไรที่ model นี้ feed เข้าไปได้บ้าง
	- img
	- vdo
	ความเร็วในการประมวลผลต่อรูปอยู่ที่ FPS = 0.12, 7.4 seconds/img (Body+face+hand) 
	ผลลัพธ์ 2D pose + face : https://drive.google.com/file/d/1CIqz2CjlCohJyify1-ps9UVKFs1ksqiG/view?usp=sharing
	ผลลัพธ์ 2D pose : https://drive.google.com/file/d/1-1ovPKDAcFTs7tPfo0zGabke5YrlKLPh/view?usp=sharing
	google drive
	- https://drive.google.com/drive/folders/1MV4mfxLWrjTmPlK3sPe2zkSWzfAZuWAN?usp=sharing (openpose2)
	- https://drive.google.com/drive/folders/1KTcH_UaUOlmy1i2zJzt96FIpYSoUmJCJ?usp=sharing (openpose)

cv2.dnn.readNetFromCaffe

OPENPOSE CHAINER MODEL 
	- Test on Google colab
	- 2Dpos (4 FPS)
	- 2Dpose+Face (1 FPS)
	Model Weight
	BODY25: http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/body_25/pose_iter_584000.caffemodel
	COCO: http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/pose_iter_440000.caffemodel
	MPI: http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel
	Face: http://posefs1.perception.cs.cmu.edu/OpenPose/models/face/pose_iter_116000.caffemodel
	Hand: http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel
<<<<<<< HEAD

openpose.exe
	Windows - Portable Demo
	bin\OpenPoseDemo.exe 
	bin\OpenPoseDemo.exe --video examples\media\video.avi
	bin\OpenPoseDemo.exe --video examples\media\video.avi --face --hand --write_json output_json_folder/
	Ref:
	https://github.com/CMU-Perceptual-Computing-Lab/openpose
	google drive
	- https://drive.google.com/drive/folders/1u_YVo8IRB-k4upLsJugrAcsk8_dSkpfH?usp=sharing
=======
>>>>>>> parent of 6b31579 (openpose_exe)
