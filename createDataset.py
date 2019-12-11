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
# train.py           # Will train a dataset and you can change classifier name in train.py @ train.py line 34
# recognizeFace.py   # Will recognize your video
#
# This is section to run file
# 1.) createDataset.py
# 2.) train.py
# 3.) recognizeFace.py

# Import the libraries
import cv2

# Set up video capture
video = cv2.VideoCapture(0)

# Define Cascade file
cascadeFile=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 'CreateDataset' function will create dataset
def CreateDataset(img, id, img_id):
    # Write file to "dataset/data.(id var).(img_id var).jpg" from img
    cv2.imwrite("dataset/data." + str(id) + "." + str(img_id) + ".jpg", img)

# 'DrawBox' function will draw a box to the facee
def DrawBox(img, classifier, scaleFactor, minNeighbors, color, text):
    # Convert to grayscale, feature variable will find face or eyes
    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(grayScale, scaleFactor, minNeighbors)

    # Define coords variable
    coords = []

    # feature was return [x, y, w, h] variable
    for (x, y, w, h) in feature:
        # Put rectangle ant text to video
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Define value to coords variable
        coords = [x, y, w, h]

    # Return [img] and [coords] variable
    return img, coords

# 'DetectAndCreateDatset' function will call 'DrawBox' functions
def DetectAndCreateDatset(img, cascadeFile, img_id):
    # Define [img] and [coords]
    img,coords= DrawBox(img, cascadeFile, 1.1, 10, (255,0,0), "Face")

    # Check if coords have 4 length value
    if len(coords) == 4:
        #img(y:y + h, x:x + w)

        # Set id for face id like (0, 1, 2, 3, 4, 5, ..)
        id = 1

        # Algorithm for crop only face and save to dataset
        result = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]

        # Call CreateDataset functions
        CreateDataset(result, id, img_id)

    # Return [img]
    return img

# Setup img_id to 0 for first pictures of face id
img_id = 0

# Loop a workspace
while True:
    # Pull video
    ret, frame = video.read()

    # frame will use DetectAndCreateDatset function
    frame = DetectAndCreateDatset(frame, cascadeFile, img_id)

    # Output
    cv2.imshow("Create Dataset", frame)

    # Add img_id for 1 counter
    img_id += 1

    # Press 'q' to exit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release a webcam task, Destroy all windows
video.release()
cv2.destroyAllWindows()
