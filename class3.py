import cv2
img=cv2.imread(r'C:\Users\Ehsan\OneDrive\Desktop\roham coding\open cv\class file\images\image3.jfif',1)
cv2.imshow('circle',img)
cv2.waitKey(0)
greyscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('g_circle',greyscale)
cv2.waitKey(0)