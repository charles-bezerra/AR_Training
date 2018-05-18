import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('charles_fronte.xml')
eye_cascade = cv2.CascadeClassifier('charles_eye.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow("Detectar Rosto")

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey + eh), (0,255,0), 2)

    cv2.waitKey(1)
    cv2.imshow('Detectar Rosto',img)

cap.release()
cv2.destroyAllWindows()
