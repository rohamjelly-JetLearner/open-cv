import cv2
import numpy as np


img=cv2.imread(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images\image3.jfif',1)
cv2.imshow('circle',img)
cv2.waitKey(0)
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('g_circle',greyscale)
cv2.waitKey(0)
blur_g=cv2.blur(greyscale,(3,3))
cv2.imshow('blurred greyscale',blur_g)
cv2.waitKey(0)
det_c=cv2.HoughCircles(blur_g,cv2.HOUGH_GRADIENT,1,1,param1=125,param2=77,minRadius=5,maxRadius=77)
h=len(det_c)
if h != 0 :
    det_c=np.uint16(np.around(det_c))
    l=len(det_c)
    for s7 in det_c[0,:]:
        s77=cv2.circle(img,(s7[0],s7[1]),s7[2],(0,0,0),5)
        cv2.imshow('detected circle',s77)
        cv2.waitKey(0)