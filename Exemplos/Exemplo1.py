import numpy as np
import cv2
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
cv2.line(img,(0,0), (150,150), (255,0,0), 15)
cv2.rectangle(img,(15,15), (200,150), (0,255,0), 5)
cv2.circle(img, (100,63),55,(0,0,255), -1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#img1 = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.polylines(img ,[pts],True,(0,255,255),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Ola foto!", (0,130), font, 5,(200,255,255), 10)
x = cv2.imshow("Antes", img)
#x = cv2.imshow("Depois", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
