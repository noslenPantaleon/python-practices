import cv2
import dlib
import numpy as np
from dataPath import DATA_PATH
import os

folder =  DATA_PATH + "/images/lenses" 
 

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

# create a window
cv2.namedWindow("images")

# define a null callback function
def null(x):
    pass

# create a trackbar 

cv2.createTrackbar("Switch_Image", "images", 0, 1, null)

 
while True:

    images = load_images_from_folder(folder)

    # get Trackbar position
    pos = cv2.getTrackbarPos("Switch_Image", "images")
    if pos == 0:
        cv2.imshow("images", images[1])
    elif pos == 1:
        cv2.imshow("images", images[2])
    key = cv2.waitKey(1) & 0xFF
    # press 'q' to quit the window
    if key == ord('q'):
        break




cv2.waitKey(0)
cv2.destroyAllWindows() 