import cv2
import numpy as np
from dataPath import DATA_PATH


imgCromakey =  DATA_PATH + "/images/croma.jpg"
videoPath = DATA_PATH + "/images/greenscreen-demo.mp4"

# Create emty image
panel = np.zeros ([100, 700], np.uint8)

# Create windows panel
cv2.namedWindow ("panel")

def trackbar(x):
    pass

cv2.createTrackbar("L - h", "panel", 0, 179, trackbar)
cv2.createTrackbar("U - h", "panel", 179, 179, trackbar)
cv2.createTrackbar("L - s", "panel", 0, 255, trackbar)
cv2.createTrackbar("U - s", "panel", 255, 255, trackbar)
cv2.createTrackbar("L - v", "panel", 0, 255, trackbar)
cv2.createTrackbar("U - v", "panel", 255, 255, trackbar)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(videoPath)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # change video color space to hsv
    hsv = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    # get data from trackbar
    l_h = cv2.getTrackbarPos ("L - h", "panel")
    u_h = cv2.getTrackbarPos ("U - h", "panel")
    l_s = cv2.getTrackbarPos ("L - s", "panel")
    u_s = cv2.getTrackbarPos ("U - s", "panel")
    l_v = cv2.getTrackbarPos ("L - v", "panel")
    u_v = cv2.getTrackbarPos ("U - v", "panel")

    # create color ranges
    lower_green = np.array ([l_h, l_s, l_v])
    upper_green= np.array ([u_h, u_s, u_v])
    
    # create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv= cv2.bitwise_not(mask)

    # add frame and mask
    bg = cv2.bitwise_and(frame, frame, mask = mask)
    fg = cv2.bitwise_and(frame, frame, mask = mask_inv)

    cv2.imshow("fg", fg)
    cv2.imshow("bg", bg)
    # cv2.imshow("panel", panel)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

cap.release ()
cv2.destroyAllWindows ()

