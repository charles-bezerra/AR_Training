import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    cv2.waitKey(2)
    cv2.imshow("Test", img)
cv2.destroyAllWindows() 

    
