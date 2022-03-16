import cv2
import time
import numpy as np

v = cv2.VideoCapture(0)
img = cv2.imread('me.jpg')
while True:
    ret,frame=v.read()
    print(frame)
    frame=cv2.resize(frame,(640,480))
    img = cv2.resize(frame,(640,480))
    ub = np.array([104,153,70])
    lb = np.array([30,30,0])
    mask = cv2.inRange(frame,lb,ub)
    r = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-r
    f = np.where(f==0,img,f)
    cv2.imshow('video',frame)
    cv2.imshow(mask,f)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
v.release()
cv2.destroyAllWindows()
        
