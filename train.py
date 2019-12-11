#!/usr/bin/python3

# OpenCV Face Recognition
# Made by Pawat Saengduan
#
# This is section to expand about all file
# dataset/           # Will be save dataset images
# createDataset.py   # Will create dataset
# *[classifier].py   # I'm not sure about file name but you can rename it in code @ train.py -
# in *[classifier].py will save about classifier data
#
# haarcascade_frontalface_default.xml  # It's a standard face detection this will be use to create dataset @ createDataset.py
# train.py           # Will train a dataset and you can change classifier name in train.py @ train.py line 52
# recognizeFace.py   # Will recognize your video
#
# This is section to run file
# 1.) createDataset.py
# 2.) train.py
# 3.) recognizeFace.py

# Import the libraries
from PIL import Image
import numpy as np
import cv2
import os

# 'TrainClassifier' function will train a dataset
def TrainClassifier(data_dir):
    # Use 'OS' library for join dataset folder
    path = [os.path.join (data_dir, f) for f in os.listdir(data_dir)]

    # Define the variable
    faces = []
    ids = []

    # Use for loop to read and feed data to arrays
    for image in path:
        img = Image.open(image).convert("L")
        imageNp=np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)

    # ids variable will equals ids in numpy arrays
    ids = np.array(ids)

    # clf variable equals LBPH Face Recognizer Algorithm
    clf = cv2.face.LBPHFaceRecognizer_create()

    # Train dataset
    clf.train(faces, ids)

    # Write to file
    clf.write("classifierPutt.xml")

# Call functions
TrainClassifier("dataset")
