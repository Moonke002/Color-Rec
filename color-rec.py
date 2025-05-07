import cv2 as cv


cam = cv.VideoCapture(0) #opens default cam

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


    print(pix_cent) #displays color
    cv.putText(frame, color, (15, 50), 2, 1.5, (0,0,0), 2)
    cv.circle(frame, (cx,cy),10, (0, 0, 255), 5) # red circle on mid screen

    cv.imshow("Webcam", frame)
    key = cv.waitKey(1)
    if key == 27 or key == ord("q"): #esc or q to break
        break

cam.release()
cv.destroyAllWindows()


