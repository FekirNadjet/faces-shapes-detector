import cv2
import numpy as np
img = cv2.imread("Resources/test2.png")
print(img.shape)
width,height=186,271
pts1=np.float32([[120,0],[200,0],[120,120],[200,120]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)
