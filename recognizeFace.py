# Source code from [Kong Ruksiam] modify [Pawat Saengduan]

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
import cv2

# Set up video capture
video = cv2.VideoCapture(0)

# Define Cascade file
cascadeFile=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 'DrawBox' function will draw a box to the facee
def DrawBox(img, classifier, scaleFactor, minNeighbors, color, clf):
    # Convert to grayscale, feature variable will find face or eyes
    grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    feature = classifier.detectMultiScale(grayScale, scaleFactor, minNeighbors)

    # Define coords variable (and some debug variable)
    coords = []
    # faceResults = ""

    # feature was return [x, y, w, h] variable
    for (x, y, w, h) in feature:
        # Put a rectangle to video
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)

        # Main Code for Recognition
        # id and con variable was be Define

        # id = face id
        # con = confidence

        id, con = clf.predict(grayScale[y:y+h, x:x+w])

        # If id equals face 1
        if id == 1:
            # If confidence less than or equal 42 (True) Insert text this person is known: (False) Inser text this person is unknown
            if con <= 42:
                # Put text to the video
                cv2.putText(img, "Pawat", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

                # Define variable for debug mode
                # faceResults = "Pawat"
            else:
                # Put text to the video
                cv2.putText(img, "Unknown", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                # Define variable for debug mode
                # faceResults = "Unknown"

        # If id equals face 1
        elif id == 2:
            # If confidence less than or equal 42 (True) Insert text this person is known: (False) Inser text this person is unknown
            if con <= 42:
                # Put text to the video
                cv2.putText(img, "Person 2", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                # Define variable for debug mode
                # faceResults = "Person 2"
            else:
                # Put text to the video
                cv2.putText(img, "Unknown", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                # Define variable for debug mode
                # faceResults = "Unknown"

        # If not match with all id
        else:
            # Put text to the video
            cv2.putText(img, "Unknown", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            faceResults = "Unknown"

        # Confidence percent will be print ( I disabled it, You can enable)
        """
        if con < 100:
            con = "  {0}%".format(round(100 - con))
        else:
            con = "  {0%}".format(round(100 - con))

        print(con)
        """
        # Print debug value
        # print(faceResults + " " + str(con) + " id " + str(id))
        # Main Code for Recognition

        # Define value to coords variable
        coords = [x, y, w, h]

    # Return [img] and [coords] variable
    return img, coords

# 'DetectAndClassifier' function will call 'DrawBox' functions
def DetectAndClassifier(img, cascadeFile, img_id, clf):
    # Define [img] and [coords]
    img,coords = DrawBox(img, cascadeFile, 1.1, 10, (255,0,0), clf)

    # Check if coords have 4 length value
    if len(coords) == 4:
        #img(y:y + h, x:x + w)

        # Unknown variable just a simple variable LMAOs
        id = 1

        # Algorithm for crop only face
        result = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]

    # Return [img]
    return img

# Setup img_id to 0 for first pic
img_id = 0

# clf variable equals LBPH Face Recognizer Algorithm
clf = cv2.face.LBPHFaceRecognizer_create()

# clf read a classifier file example (classifier)
clf.read("classifier.xml")

# Loop a workspace
while True:
    # Pull video
    ret, frame = video.read()

    # frame will use 'DetectAndClassifier' function
    frame = DetectAndClassifier(frame, cascadeFile, img_id, clf)

    # Output
    cv2.imshow("Face Recognition", frame)

    # Add img_id for 1 images
    img_id += 1

    # Press 'q' to exit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release a webcam task, Destroy all windows
video.release()
cv2.destroyAllWindows()
