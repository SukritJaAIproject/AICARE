## OpenPose

This is essentially a slightly modified version of OpenPose as described in [this LearnOpenCV tutorial](https://www.learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/). You can also get a C++ version there.

### Running it:
* You need OpenCV version **3.4.1** or newer. I tested it with version 3.4.3.
* You can use the **COCO** model or the **MPI** model for the pose extraction, the models are not included here due to their size. Therefore you need to run ```getModels.sh``` first. 
(NOTE: For some reason, it didn't download all the necessary files for me sometimes. I had to manually download ```pose_deploy_linevec_faster_4_stages.prototxt``` from [HERE](https://github.com/CMU-Perceptual-Computing-Lab/openpose/tree/master/models/pose/mpi) and add it to ```/pose/mpi```.)
* The script currently has no parameters, simply run ```python OpenPoseImage.py```. Switching between MPI and COCO and loading a different image has to be changed in the code of ```OpenPoseImage.py```.
