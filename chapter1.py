import cv2

##import and read an image
# img = cv2.imread("Resources/test1.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(2000)

##import and read a video
# vid = cv2.VideoCapture("Resources/video.mp4")
# while True:
#     success, img = vid.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF ==ord("q"):
#         break

#using a webCam
vidCam = cv2.VideoCapture(0)
vidCam.set(3,640) #weight
vidCam.set(4,480) #height
vidCam.set(10,100)#brightness

while True:
    success, img = vidCam.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break




