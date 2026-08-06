import cv2
import os

haar=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\haarcascade_frontalface_default.xml'
face=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg'

sf=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg\roham'
path=os.path.join(face,sf)
if not os.path.isdir(path):
    os.mkdir(path)
cas=cv2.CascadeClassifier(haar)
cam=cv2.VideoCapture(0)
for i in range(30):
    camvalid,camimage=cam.read()
    # print(camimage)
    camgrey=cv2.cvtColor(camimage,cv2.COLOR_BGR2GRAY)
    print(camgrey)
    rect=cas.detectMultiScale(camgrey,1.2,3)
    print(rect)
    # x=rect[0][0]
    # y=rect[0][1]
    # width=rect[0][2]
    # height=rect[0][3]
