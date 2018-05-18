
#python 2.7.12
#ubuntu
#OpenCV 3.2.0
import cv2
import numpy as np
class Cam:
    __stop = None
    def __init__(self, cv2,np):
        self.cv2 = cv2
        self.np = np
        self.cv2.namedWindow("Camera")
        self.cap = self.cv2.VideoCapture(0)
        self.photo = self.cv2.imread("Data/pikachu.png")
        self.face_cascade = self.cv2.CascadeClassifier("Data/haarcascade_frontalface_default.xml")
    def show(self):
        while True:
            ret, img = self.cap.read()
            linha, coluna, canal = self.photo.shape
            roi = img[0:linha, 0:coluna]
            img2cinza = self.cv2.cvtColor(self.photo,self.cv2.COLOR_BGR2GRAY)
            cinza = self.cv2.cvtColor(img, self.cv2.COLOR_BGR2GRAY)
            ret, mascara = self.cv2.threshold(img2cinza, 0, 255, self.cv2.THRESH_BINARY)
            mascara_inv = self.cv2.bitwise_not(mascara) #convert todos os pixels da imagem para negativo
            img1_bg = self.cv2.bitwise_and(roi,roi,mask = mascara_inv)
            img2_fg = self.cv2.bitwise_and(self.photo,self.photo,mask = mascara)
            face = self.face_cascade.detectMultiScale(cinza, 1.3 ,5)
            for (x, y, w, h) in face:
                self.cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255),2)
                soma = self.cv2.add(img1_bg,img2_fg)
                img[0:linha, 0:coluna ] = soma
            self.cv2.imshow("Camera", img)
            k = self.cv2.waitKey(1)
            if k == 27:
                break
        self.cv2.destroyAllWindows()
        self.cap.release()
class main:
    if __name__ == '__main__':
        cam = Cam(cv2,np)
        cam.show()
