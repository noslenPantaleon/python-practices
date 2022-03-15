# Required modules
import cv2
import numpy as np
import matplotlib.pyplot as plt
from dataPath import DATA_PATH


imagePath = DATA_PATH + "/images/picture.jpg"

min_HSV = np.array([0, 58, 30], dtype = "uint8")
max_HSV = np.array([33, 255, 255], dtype = "uint8")
# Get pointer to video frames from primary device
image = cv2.imread(imagePath, 1)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)

skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)
# skinHSV = np.hstack([image, skinHSV]))
cv2.imshow ("skin", skinHSV )

cv2.waitKey(0)