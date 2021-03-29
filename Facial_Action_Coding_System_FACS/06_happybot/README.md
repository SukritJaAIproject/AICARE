# FACS_recognition
This repository applies a neural network to frontal face image sequences to find facial Action Units (AUs). AUs, part of the Facial Action Coding System ([FACS](https://en.wikipedia.org/wiki/Facial_Action_Coding_System)), are a compelling way to analyze facial expressions, as the basic emotions (happiness, sadness, anger, fear, surprise, disgust, and contempt) have AUs in common. Paul Ekman, who established FACS, ran studies showing that people in isolated, rural communities recognize facial expressions just as people in cities recognize facial expressions. The [research](http://psycnet.apa.org/record/1971-07999-001) suggests some facial expressions are universal. 

The algorithm identifies AUs 1, 2, 4, 5, 9, 12, 15, 17, 20, 25, and 27.

## Motivation
Many businesses want to provide something to a customer that will make them happier, but we don't have good ways to measure how happy a person is. I wanted to get a taste of how computer vision could identify a person's feeling. Computer vision is a deep field, and I finish my ambitious project wiser and hopeful. 

I was happy that my background in physics and programming for lab provided me with sufficient tools to learn the novel aspects of this project. Many algorithms were new to me and forums, books, and papers guided me in the right direction. 

## Background
I used the [CK+ Dataset](http://www.pitt.edu/~emotion/ck-spread.htm) because it was available and had labelled AUs and some labelled basic emotions. The CK+ Dataset consists of 593 image sequences of 123 subjects. All sequences start at neutral facial expression and end at peak facial expression. All sequences are coded with AUs and corresponding intensities. 327 sequences are labelled for basic emotions. 

I started the project reading recent papers about convolutional neural networks, such as Modeling Spatial and Temporal Cues for
Multi-label Facial Action Unit Detection by [Chu, Torre and Cohn](https://arxiv.org/abs/1608.00911). They paired a CNN with an LSTM so that the occurrence of one AU changes the probability of the occurence of the another. I think CNNs and LSTMs are promising for identifying emotions in the wild, as CNNs are tolerant of translation and rotations of faces, and since CNNs struggle to capture long term dependencies, LSTMs are appropriate. I appreciate the usefulness of CNNs, and the paper on how the layers work by [Zeiler](https://arxiv.org/abs/1311.2901) was illuminating, but I was drawn to the simpler methods of SVM, AdaBoost, and feed-forward MLP. 

In [Kotsia and Pitas' paper](https://ieeexplore.ieee.org/document/4032815/), they used a modified SVM and the displacement of facial landmarks from a Candide Grid over a sequence of images to classify AUs and basic emotions. [Bartlett's team](https://ieeexplore.ieee.org/document/1398364/) convolved facial images with Gabor filters, and classified them with AdaBoost, SVM, and Linear Discriminant Analysis. AdaBoost with SVM performed best. I decided to follow [Tian, Kanade, and Cohn's paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4157835/), which found AUs by calculating the displacement of facial landmarks over time and appling Canny edge detectors to look for wrinkles in the corners of the eye or between the eyebrows and inputting the data to a feed-forward MLP. 

## Methods
The problem I aimed to solve was: Can I make a script to identify AUs and emotions? I used the dlib library in Python to track facial features in the CK+ dataset. Following Tian's paper, the script calculated key distances such as distance between the eyebrows, distance between the lips, and the distance between the corner of the lips and the eyes. With OpenCV, I used the Canny edge detection on the corners of the eyes and between the brows to find the deepening of lines and furrows. Lines and furrows are a transient feature. Adults will have more wrinkles than children and, alone, they are not a reliable indicator of AUs or emotions. However, for this dataset, adding the transient features increased accuracy. 

The neural network was written in tensorflow and summarized in tensorboard. I was amused by the time it took me to concatenate a matrix, but I was pleased by how fit the module is for machine learning. 

## Evaluating Accuracy
I used a binary multiclass classifier, which means the algorithm forces a decision as to whether there is an AU or not. The CK+ database is unbalanced for FACS analysis so I weighted the presence of an AU I'm looking for, positive values, more than the absense of an AU, negative values. Accuracy, in this context, is a misnomer as it will artificially inflate when the algorithm match null values. The test of accuracy is the true positive rate (TPR). 

### Accuracy for Detecting Lower Facial Features
![Figure Not Found!](/img/bot_tpr23.png)

It was interesting that the testing TPR passed the training TPR. I've never seen that happen before. A quarter of the samples were used for testing. If the database were larger, the additional testing samples would match the TPR of the testing and training. It does give me confidence that the model is not overfitting.

### Biases of 2nd Fully Connected Layer
![Figure Not Found!](/img/bot_activation.png)

I like Tensorflow for this visualization. It's very useful to be able to see what every layer is doing. 

### Cross Entropy Loss function for Lower Facial Features
![Figure Not Found!](/img/bot_xent23.png)

The loss function show go toward zero and it does. 

Two separate neural networks analyzed the top half of the face and the lower half of the face. The upper model had a TPR 87% and the lower model had a TPR of 91%, which averages to 89% TPR. I found the upper model performed best with six layers, and the lower with only two, which I assume is because the facial actions in the lower part of the face move a greater distance and are easier to detect. This accuracy is comparable to Tian's paper, and Tian's group calculated accuracy in the same way. However, Tian used a dataset in addition to CK+, the Ekman-Hager Facial Action Dataset. I saw, from the confusion matrix, that some AUs were detected more reliably than others. After some tinkering with the input parameters and the weights of the loss function, nothing changed, and I deduced that the problem was limited data and I eliminated them from the classification. The AUs found were sufficient to classify basic emotions on live video. 

Here's a pic of me smiling. There are a few extra AUs because this was an earlier version with about 80% accuracy, but it still read my facial expression. I was happy that the model worked outside of the CK+ dataset. 

![Beautiful Image Not Found!](/img/face_pic.png)
