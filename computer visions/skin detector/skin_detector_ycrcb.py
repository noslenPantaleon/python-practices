import cv2
import numpy as np
import matplotlib.pyplot as plt
from dataPath import DATA_PATH


imagePath = DATA_PATH + "/images/picture.jpg"
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

# Get pointer to video frames from primary device
image = cv2.imread(imagePath, 1)
imageYCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)

cv2.imwrite("/images/ycrcb.png", np.hstack([image,skinYCrCb]))
cv2.imshow ("skin", skinYCrCb )
# cv2.imshow ("min_YCrCb", min_YCrCb )
# cv2.imshow ("max_YCrCb", max_YCrCb )


cv2.waitKey(0)