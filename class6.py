import cv2
import os

haar=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\haarcascade_frontalface_default.xml'
face=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg'

sf=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg\roham'
path=os.path.join(face,sf)
if not os.path.isdir(path):
    os.mkdir(path)
cas=cv2.CascadeClassifier(haar)
print(cas.empty())
cam=cv2.VideoCapture(0)
for i in range(30):
    camvalid,camimage=cam.read()
    # print(camimage)
    camgrey=cv2.cvtColor(camimage,cv2.COLOR_BGR2GRAY)
    print(camgrey)
    rect=cas.detectMultiScale(camgrey,scaleFactor=1.1,minNeighbors=3,minSize=(30,30))
    print(rect)
    # x=rect[0][0]
    # y=rect[0][1]
    # width=rect[0][2]
    # height=rect[0][3]
    # cv2.imshow('image',camimage)
    # cv2.waitKey(0)
