import cv2
import numpy as np
from dataPath import DATA_PATH


imgCromakey =  DATA_PATH + "/images/croma.jpg"
videoPath = DATA_PATH + "/images/greenscreen-demo.mp4"
webcam = True
cap= cv2.VideoCapture (0)
cap2 = cv2.VideoCapture(videoPath)

panel = np.zeros ([100, 700], np.uint8)
cv2.namedWindow ("panel")

def nothing(x):
    pass

cv2.createTrackbar("L - h", "panel", 0, 179, nothing)
cv2.createTrackbar("U - h", "panel", 179, 179, nothing)
cv2.createTrackbar("L - s", "panel", 0, 255, nothing)
cv2.createTrackbar("U - s", "panel", 255, 255, nothing)
cv2.createTrackbar("L - v", "panel", 0, 255, nothing)
cv2.createTrackbar("U - v", "panel", 255, 255, nothing)


while True:

    #reading source image, or webcam
    if webcam: 
        success, frame = cap.read ()
    else:    
        if (cap2.isOpened()== False):
                print("Error opening video stream or file")

        while(cap2.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:      
                frame = np.array(frame)
                cv2.imshow ("frame", frame)
            _, frame = cap.read()
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
 
    l_h = cv2.getTrackbarPos ("L - h", "panel")
    u_h = cv2.getTrackbarPos ("U - h", "panel")
    l_s = cv2.getTrackbarPos ("L - s", "panel")
    u_s = cv2.getTrackbarPos ("U - s", "panel")
    l_v = cv2.getTrackbarPos ("L - v", "panel")
    u_v = cv2.getTrackbarPos ("U - v", "panel")

    lower_green = np.array ([l_h, l_s, l_v])
    upper_green= np.array ([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv= cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(frame, frame, mask = mask)
    fg = cv2.bitwise_and(frame, frame, mask = mask_inv)

    cv2.imshow("fg", fg)
    cv2.imshow("bg", bg)
    cv2.imshow("panel", panel)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

cap.release ()
cv2.destroyAllWindows ()




