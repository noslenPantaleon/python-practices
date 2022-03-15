import cv2
import numpy as np
from dataPath import DATA_PATH

imagePath2 = DATA_PATH + "/images/croppedimage.jpg"
imagePath = DATA_PATH + "/images/picture.jpg"

cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
image = cv2.imread(imagePath, 1)
oriImage = image.copy()

windowName= "crop"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            cv2.imwrite(imagePath2 , roi) 
           
           

cv2.setMouseCallback (windowName, mouse_crop)





while True:
    i = image.copy()
 
    if not cropping:
        cv2.imshow(windowName, image)
    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow(windowName, i)

    c = cv2.waitKey(10)
# close all open windows
    if c==27:
            break
cv2.destroyAllWindows()