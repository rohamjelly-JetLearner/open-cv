import cv2
import os
from PIL import Image
path=r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images'
os.chdir(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images')
mwid=0
mheight=0
imgs=[]
for i in os.listdir('.'):
    if i.endswith(('.webp')):
        imgs.append(i)
for i in imgs:
    img=Image.open(os.path.join(path,i))
    w,h=img.size
    mwid=mwid+w
    mheight=mheight+h
l=len(imgs)
mwid=mwid//l
mheight=mheight//l
print(mwid,mheight)
for i in imgs:
    img=Image.open(os.path.join(path,i))
    imgr=img.resize((mwid,mheight))
    imgr.save(i,'png',quality=97)
vid='777777.mp4'
imgs=[]
for i in os.listdir('.'):
    if i.endswith(('.webp')):
        imgs.append(i)
print(imgs)
frame=cv2.imread(os.path.join(path,imgs[0]))
video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'mp4v'),0.77777777777,(mwid,mheight))
for i in imgs:
    video.write(cv2.imread(os.path.join(path,i)))
video.release()
    