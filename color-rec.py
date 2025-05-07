import cv2 as cv
import numpy as np

def nothing(x):
    pass

cam = cv.VideoCapture(0) #opens default cam

cv.namedWindow("HSV Frame")
for name, max_val in zip(("H", "S", "V"), (179, 255, 255)):
    cv.createTrackbar(name, "HSV Frame", 0, max_val, nothing)

img_hsv = np.zeros((250, 500 ,3), np.uint8) #blank image

h = cv.getTrackbarPos("H", "HSV Frame")
s = cv.getTrackbarPos("S", "HSV Frame")
v = cv.getTrackbarPos("V", "HSV Frame")


while True: #frame loop
    ret, frame = cam.read()
    if not ret:
        break

    hsv_frame = cv.cvtColor(frame, cv.COLOR_RGB2HSV) #converts frame from rgb to hsv
    height, width, channels = frame.shape
    cv.normalize(frame, frame, 0, 255, cv.NORM_MINMAX)

    #center point
    cx = width //2
    cy = height // 2

    pix_cent = hsv_frame[cy, cx]
    hue_val = pix_cent[0]
    sat_val = pix_cent[1]
    v_val = pix_cent[2]

    # color scales
    color = "Unknown"
    if sat_val < 30 and v_val > 200:
        color = "White"
    elif hue_val < 1:
        color = "Black"
    elif hue_val < 29:
        color = "Blue"
    elif hue_val < 40:
        color = "Cyan"
    elif hue_val < 84:
        color = "Green"
    elif hue_val < 96:
        color = "Orange"
    elif hue_val < 125:
        color = "Red"
    elif hue_val < 134:
        color = "Pink"
    elif hue_val < 152:
        color = "Violet"
    elif hue_val < 159:
        color = "Purple"
    elif hue_val < 171:
        color = "Blue"
    else:
        color = "Unknown"

    h = cv.getTrackbarPos("H", "HSV Frame")
    s = cv.getTrackbarPos("S", "HSV Frame")
    v = cv.getTrackbarPos("V", "HSV Frame")

    selected_hsv = np.uint8([[[h, s, v]]])
    selected_rgb = cv.cvtColor(selected_hsv, cv.COLOR_HSV2RGB)[0][0]

    # compares selected color with on screen color
    h_diff = min(abs(h - hue_val), 180 - abs(h - hue_val))
    s_diff = abs(s - sat_val)
    v_diff = abs(v - v_val)


    if h_diff < 15 and s_diff < 40 and v_diff < 40:
        match_text = "Match"
    else:
        match_text = "No Match"

    print(pix_cent) #displays color
    cv.putText(frame, color, (15, 50), 2, 1.5, (0,0,0), 2)
    
    # red circle on mid screen
    cv.circle(frame, (cx,cy),10, (0, 0, 255), 5) 

    # draw selected color preview box
    cv.rectangle(frame, (10, height - 60), (110, height - 10), selected_rgb.tolist(), -1)

    # draw match or no match text
    cv.putText(frame, match_text, (130, height - 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)


    cv.imshow("HSV Frame", frame)
    key = cv.waitKey(1)
    if key == 27 or key == ord("q"): #esc or q to break
        break

cam.release()
cv.destroyAllWindows()


