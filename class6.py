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
number=1
for i in range(30):
    camvalid,camimage=cam.read()
    camgrey=cv2.cvtColor(camimage,cv2.COLOR_BGR2GRAY)
    rect=cas.detectMultiScale(camgrey,scaleFactor=1.1,minNeighbors=3,minSize=(30,30))
    print(rect)
    for (x,y,w,h) in rect:
        face=camgrey[y:y+h,x:x+w]
        cv2.imwrite('%s/%s.png'%(sf,number),face)
    number+=1