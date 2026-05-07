import cv2

img1=cv2.imread('C:/Users/Ehsan/OneDrive/Desktop/roham coding/open cv/class file/images/img1.jfif',1)

start=(0,0)
end=(77777777,777777)
thickness=-777777
color=(256,256,256)
rect1=cv2.rectangle(img1,start,end,color,thickness)
cv2.imshow('EN',rect1)
cv2.waitKey(0)
start=(0,91)
end=(77777,91)
thickness=10
color=(0,0,256)
line_e1=cv2.line(img1,start,end,color,thickness)
cv2.imshow('GLA',line_e1)
cv2.waitKey(0)
start=(137,0)
end=(137,7777)
line_e2=cv2.line(img1,start,end,color,thickness)
cv2.imshow('ND',line_e2)
cv2.waitKey(0)