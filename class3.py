import cv2
import numpy as np

img=cv2.imread(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images\image4.png',1)
img=cv2.resize(img,(200,200))
cv2.imshow('circle',img)
cv2.waitKey(0)
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('g_circle',greyscale)
cv2.waitKey(0)
blur_g=cv2.blur(greyscale,(3,3))
cv2.imshow('blurred greyscale',blur_g)
cv2.waitKey(0)
det_c=cv2.HoughCircles(blur_g,cv2.HOUGH_GRADIENT,1,1,param1=125,param2=47,minRadius=1,maxRadius=77)
h=len(det_c)
if h != 0 :
    det_c=np.uint16(np.around(det_c))
    l=len(det_c)
    for s7 in det_c[0,:]:
        s77=cv2.circle(img,(s7[0],s7[1]),s7[2],(0,0,0),5)
        cv2.imshow('detected circle hough',s77)
        cv2.waitKey(0)
    
param=cv2.SimpleBlobDetector_Params()
param.filterByArea=True
param.minArea=10
param.filterByCircularity=True
param.minCircularity=0.25
param.filterByConvexity=True
param.minConvexity=0.25
param.filterByInertia=True
param.minInertiaRatio=0.25
det=cv2.SimpleBlobDetector_create(param)
key_p=det.detect(img)
cir_det=cv2.drawKeypoints(img,key_p,img,(0,0,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
txt=cv2.putText(img,str((len(key_p))),(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),3)
CIR=cv2.imshow('detected circles simple',cir_det)
cv2.waitKey(0)
cv2.destroyAllWindows()
