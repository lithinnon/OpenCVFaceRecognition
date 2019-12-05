# Face Recognition with OpenCV
In this project we'll make a Face Recognition using Python

Libraries:
1. Numpy
2. OpenCV & OpenCV Contrib
3. Pillow

### Explain the file one-by-one
1. `dataset/`                             *Please Create because this folder will store all face dataset*
2.` haarcascade_frontalface_default.xml`  Standard face detection for get dataset
3. `CreateDataset.py`                     Create face dataset
4. `train.py`                             This file will train dataset
5. `[classifier.xml]`                     This file will create by `train.py` so u can change file name in code or rename it
6. `recognizeFace.py`                     This file will run face recognition

### Section to run file
1. Create `dataset/` folder first (if not exist)
2. Run `CreateDataset.py` to create face dataset
3. Run `train.py` to train dataset and save to `[YOURCLASSIFIERNAME].xml`
4. Run `recognizeFace.py` to run the face recognition by use `[YOURCLASSIFIERNAME].xml`
( If you change `[YOURCLASSIFIERNAME].xml` to another name, Please change file name @ `recognizeFace.py` line 32)
