import cv2
import os 

cherry=cv2.imread('C:/Users/Ehsan/OneDrive/Desktop/roham coding/open cv/class file/saved imgs/cherry.png',1)
cv2.imshow('cherry',cherry)
cv2.waitKey(0)
cerry=cv2.imread('C:/Users/Ehsan/OneDrive/Desktop/roham coding/open cv/class file/saved imgs/cherry.png',2)
cv2.imshow('cherry in greyscale',cerry)
cv2.waitKey(0)
saved='C:/Users/Ehsan/OneDrive/Desktop/roham coding/open cv/class file/saved imgs'
os.chdir(saved)
cv2.imwrite('cherry.png',cherry)