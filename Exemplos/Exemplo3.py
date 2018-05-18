import cv2
import numpy as np
cap = cv2.VideoCapture(0) #Captura os frames de determinadas fontes, seja elas de cameras ou videos pesistidos
cv2.namedWindow("Test") #Criu uma janela com o nome "Test"
while True:
    ret,img = cap.read()
    cv2.waitKey(1)
    cv2.imshow("Test", img)
cv2.destroyAllWindows()
