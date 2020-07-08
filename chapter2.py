import cv2
import numpy as np

img = cv2.imread("Resources/test1.jpg")
kernel = np.ones((5, 5), np.uint8)

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)#opposite of eroded
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray Image", imgGrey)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
