import cv2
import os
from PIL import Image
path=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images'
os.chdir(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images')
mwid=0
mheig=0
imgs=[]
for i in os.listdir('.'):
    if i.endswith(('.webp')):
        imgs.append(i)
