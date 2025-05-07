import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("HSV Frame")
cv.createTrackbar("H", "HSV Frame", 0, 179, nothing)
cv.createTrackbar("S", "HSV Frame", 0, 255, nothing)
cv.createTrackbar("V", "HSV Frame", 0, 255, nothing)

img_hsv = np.zeros((250, 500 ,3), np.uint8)

while True:
    h = cv.getTrackbarPos("H", "HSV Frame")
    s = cv.getTrackbarPos("S", "HSV Frame")
    v = cv.getTrackbarPos("V", "HSV Frame")

    img_hsv[:] = (h,s,v)
    img_rgb = cv.cvtColor(img_hsv, cv.COLOR_HSV2RGB)

    cv.imshow("HSV Frame", img_rgb)
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()





