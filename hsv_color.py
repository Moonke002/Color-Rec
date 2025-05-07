#this code uses opencv to create an hsv color slider to display the different values for each hsv color

import cv2 as cv
import numpy as np

def nothing(x): #dummy callback
    pass

#creates window and trackbar
cv.namedWindow("HSV Frame")
for name, max_val in zip(("H", "S", "V"), (179, 255, 255)):
    cv.createTrackbar(name, "HSV Frame", 0, max_val, nothing)

img_hsv = np.zeros((250, 500 ,3), np.uint8) #blank image and size


#gets trackbar position
while True:
    h = cv.getTrackbarPos("H", "HSV Frame")
    s = cv.getTrackbarPos("S", "HSV Frame")
    v = cv.getTrackbarPos("V", "HSV Frame")

    img_hsv[:] = (h,s,v) #sets pixels to hsv colors
    img_rgb = cv.cvtColor(img_hsv, cv.COLOR_HSV2RGB) #converts hsv to rgb for better display

    cv.imshow("HSV Frame", img_rgb)
    key = cv.waitKey(1) #waitkey to keep open and running
    if key == 27 or key == ord("q"): #escape/q to break
        break

cv.destroyAllWindows()
