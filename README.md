# Face Recognition with OpenCV
In this project we'll make a Face Recognition using Python

Libraries:
1. Numpy
2. OpenCV & OpenCV Contrib
3. Pillow

### Explain the file one-by-one
1. `requirements.txt`                     List to install package by run `pip install -r requirements.txt`
2. `dataset/`                             *Please Create because this folder will store all face dataset*
3.` haarcascade_frontalface_default.xml`  Standard face detection for get dataset
4. `CreateDataset.py`                     Create face dataset
5. `train.py`                             This file will train dataset
6. `[classifier.xml]`                     This file will create by `train.py` so u can change file name in code or rename it
7. `recognizeFace.py`                     This file will run face recognition

### Section to run file
1. Run `pip install -r requirements.txt` for install package
2. Create `dataset/` folder first (if not exist)
3. Run `CreateDataset.py` to create face dataset
4. Run `train.py` to train dataset and save to `[YOURCLASSIFIERNAME].xml`
5. Run `recognizeFace.py` to run the face recognition by use `[YOURCLASSIFIERNAME].xml`
( If you change `[YOURCLASSIFIERNAME].xml` to another name, Please change file name @ `recognizeFace.py` line 32)
