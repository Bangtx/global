import cv2
import numpy as np

# printing each shapes by dectecting contours, categorize, corner points, area
path = "4f94bdaab13d7863212c.jpg"
img = cv2.imread(path)
# copy original image
imgContour = img.copy()

# convert into grey scale and then find edges -> corner points
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# fine edges
imgCanny = cv2.Canny(imgBlur, 50, 50)


# get contour
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # find area
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # -1 to draw all the contours
            # calculate curve length -> corners of edges and shape
            peri = cv2.arcLength(cnt, True)
            print(peri)
            # approximate corner points (how many)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            # objects cornets
            objCor = len(approx)
            # creat a bounding box around detected objects
            x, y, w, h = cv2.boundingRect(approx)
            # define objects
            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circle"
            else:
                objectType = "None"
            # write
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x + (w / 2) - 10, y + (y / 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


getContours(imgCanny)
# imgBlank = np.zeros((400,400), np.uint8)
# imgBlank = cv2.cvtColor(imgBlank, cv2.COLOR_GRAY2BGR)

imgStack = np.hstack((img, imgContour))

cv2.imshow("Stack", imgStack)
cv2.waitKey(0)
