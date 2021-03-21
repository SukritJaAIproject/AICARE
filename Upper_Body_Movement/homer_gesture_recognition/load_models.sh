#!/usr/bin/env
#Donwload openpose models and gestrec_models

mkdir -p ./models/gestrec_pretrained
mkdir -p ./models/openpose

#OPENPOSE_URL="http://posefs1.perception.cs.cmu.edu/OpenPose/models/"
#PROTO="https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/models/pose/coco/pose_deploy_linevec.prototxt"
#MODEL="pose_iter_584000.caffemodel"

#wget ${OPENPOSE_URL}${MODEL} -P ./models/openpose/

#TODO
GESTREC_URL="http://posefs1.perception.cs.cmu.edu/OpenPose/models/"

wget ${GESTREC_URL} -P ./models/gestrec_pretrained/
