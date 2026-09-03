import cv2
import os

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
            img.append(cv2.imread(img_path,0))
            labels.append(id)
            