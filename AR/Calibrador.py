import numpy as np
import cv2
import glob
def drawlines(img,corners,imgpoints):
    linhax = cv2.line(img, corners, tuble(imgpoints[0].ravel()), (255,0,0),5)
    linhay = cv2.line(img, corners, tuble(imgpoints[1].ravel()), (0,255,0),5)
    linhaz = cv2.line(img, corners, tuble(imgpoints[2].ravel()), (0,0,255),5)
    return img
cv2.namedWindow("Calibre")
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('Data/2.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)
    # If found, add object points, image points (after refining them)
    if True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        img = drawlines(img, corners2, imgpoints)
        cv2.imshow('Calibre',img)
        cv2.imwrite("Data/Result.jpg", img)
        cv2.waitKey(0)
cv2.destroyAllWindows()
