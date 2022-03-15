import numpy as np 
import cv2
from dataPath import DATA_PATH


filename = DATA_PATH + "images/picture.jpg"
img = cv2.imread(filename, 1)

# Get the image's height, width, and channels
height, width, channel = img.shape

# Create balnk HSV image
img_hsv = np.zeros((height,width,3))

# ======================================================
# IMPLEMENTATION USING OPENCV LIBRARY 
# ======================================================
#  img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ======================================================
# IMPLEMENTATION WITHOUT OPENCV LIBRARY 
# ======================================================
# CALCULATE
for i in np.arange(height):
    for j in np.arange(width):
        r = img.item(i,j,0)
        g = img.item(i,j,1)
        b = img.item(i,j,2)

        r_ = r/255.
        g_ = g/255.
        b_ = b/255.
        Cmax = max(r_,g_,b_)
        Cmin = min(r_,g_,b_)
        delta = Cmax-Cmin

        # Hue Calculation
        if delta == 0:
            H = 0
        elif Cmax == r_ :
            H = 60 * (((g_ - b_)/delta) % 6)
        elif Cmax == g_:
            H = 60 * (((b_ - r_)/delta) + 2)
        elif Cmax == b_:
            H = 60 * (((r_ - g_)/delta) + 4)

        # Saturation Calculation
        if Cmax == 0:
            S = 0
        else :
            S = delta / Cmax
        
        # Value Calculation
        V = Cmax 
        
        # Set H,S,and V to image
        img_hsv.itemset((i,j,0),int(H))
        img_hsv.itemset((i,j,1),int(S))
        img_hsv.itemset((i,j,2),int(V))

# Write image
cv2.imwrite('image_hsv.jpg', img_hsv)

# View image

imgbgr= cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR )
cv2.imshow('image', imgbgr)
cv2.waitKey(0)
cv2.destroyAllWindows()