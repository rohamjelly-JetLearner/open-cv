import cv2 
import numpy as np
vid=cv2.VideoCapture(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images\video.mp4')
bg=''
for i in range (60):
    bv,frame=vid.read()
    if bv== False:
        print('could not read this frame')
        continue
    bg=frame
bg=np.flip(bg,axis=1)
while vid.isOpened():
    bv,frames=vid.read()
    frames=np.flip(frames,axis=1)
    hsv=cv2.cvtColor(frames,cv2.COLOR_RGB2HSV)
    sr=np.array([0,120,40])
    er=np.array([100,255,255])
    mask=cv2.inRange(hsv,sr,er)
    srr=np.array([170,40,40])
    err=np.array([180,255,255])
    mask1=cv2.inRange(hsv,srr,err)
    mask2=mask1+mask
    mask3=cv2.morphologyEx(mask2,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=5)
    mask4=cv2.bitwise_not(mask3)
    result=cv2.bitwise_and(bg,bg,mask=mask3)
    result1=cv2.bitwise_and(frames,frames,mask4)
    result2=result+result1
    res=cv2.imshow('image',result2)

