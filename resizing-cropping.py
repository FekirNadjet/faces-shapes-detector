import cv2

img = cv2.imread("Resources/test1.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))# weight then the height

imgCropped=img[0:200,200:500]#height then the weight

cv2.imshow("image", img)
cv2.imshow("image Resize", imgResize)
cv2.imshow("image Cropped", imgCropped)#using matrix not cv2
cv2.waitKey(0)
