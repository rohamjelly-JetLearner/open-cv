import cv2
import os
import numpy as np

haar=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\haarcascade_frontalface_default.xml'
face=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg' 
img=[]
labels=[]
id=-1
dictionary={}
for folder,subfolder,files in os.walk(face):
    for fold in subfolder:
        id+=1
        dictionary[id]=fold
        fold_path=os.path.join(face,fold)
        for image in os.listdir(fold_path):
            img_path=os.path.join(fold_path,image)
            img_=cv2.imread(img_path,0)
            img_=cv2.resize(img_,(200,200))
            img.append(img_)
            labels.append(id)

imgl=np.array(img)
label_l=np.array(labels)
mod=cv2.face.LBPHFaceRecognizer_create()
mod.train(imgl,label_l)
facec=cv2.CascadeClassifier(haar)
web=cv2.VideoCapture(0)
while True:
    w_b,imgw=web.read()
    imgw=cv2.cvtColor(imgw,cv2.COLOR_BGR2GRAY)
    rect=facec.detectMultiScale(imgw,scaleFactor=1.1,minNeighbors=3,minSize=(30,30))
    print(rect)
    for (x,y,w,h) in rect:
        face=imgw[y:y+h,x:x+w]
        predict=mod.predict(face)
        cv2.rectangle(imgw,(x,y),(x+w,y+h),(0,0,0),1)
    cv2.imshow('face recogniser',imgw)
