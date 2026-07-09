import cv2
import os

haar=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\haarcascade_frontalface_default.xml'
face=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg'

sf=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\face recognition\faceimg\roham'
path=os.path.join(face,sf)
if not os.path.isdir(path):
    os.mkdir(path)
    