import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)  # will give us the extrenal contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # imgContour is a copy of the original images we will draw our contours there with blue color
        if area > 500:  # for example we will not detect the contours of the letters
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # -1 because we want to draw all the contours index
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)  # for each contour we will have the points
            print(len(approx))  # number of points so we can detect wich shape is
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # the type of the shape
            if objCor == 3:
                ObjectType = "Tri"
            elif objCor == 4:
                ratio = w / float(h)
                if ratio > 0.95 and ratio < 1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"

            else:
                ObjectType = "None"
            cv2.putText(imgContour, ObjectType, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5,
                        (0, 255, 255), 2)  # the tird parameter is where we want to put the text

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw boxes around our shapes


img = cv2.imread("Resources/test4.png")
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur], [imgCanny, imgContour, imgBlank]))
cv2.imshow("stack", imgStack)

cv2.waitKey(0)
