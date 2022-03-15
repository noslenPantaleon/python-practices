import cv2
import numpy as np
from dataPath import DATA_PATH
# def Embossed  (img):
    
#     kernel = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
#     img_sharpen = cv2.filter2D(img, -1, kernel)
#     img_sharpen = cv2.bitwise_and(img, img, mask= img_sharpen)
#     return img_sharpen


# from scipy.interpolate import UnivariateSpline
# def LookupTable(x, y):
#   spline = UnivariateSpline(x, y)
#   return spline(range(256))

# def Summer(img):
#     increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
#     decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
#     blue_channel, green_channel,red_channel  = cv2.split(img)
#     red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
#     blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
#     sum= cv2.merge((blue_channel, green_channel, red_channel ))
#     return sum
# def cartoonify2(img):
    
#     th, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#     color = cv2.bilateralFilter (img, 2, 300, 300)
#     thresh =cv2.cvtColor (thresh, cv2.COLOR_BGR2GRAY)
#     cannyEdges = cv2.Canny(img, 5, 200)
#     cartoonify2 = cv2.bitwise_and (color, color, mask= cannyEdges)
#     return cartoonify2
    

# Read an image in grayscale
imagePath = DATA_PATH + '/images/picture.jpg'
src = cv2.imread(imagePath, 3)
gray = cv2.cvtColor (src, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur (gray, 5)

ddepth = cv2.CV_16S
kernel_size = 1

imgSize= src.shape
panel = np.zeros ( [imgSize [0],imgSize[1] ], np.uint8)
hsv = cv2.cvtColor (src, cv2.COLOR_BGR2HSV)


# Find Canny edges
cannyEdges = cv2.Canny(src, 5, 200)
# cannyEdges= cv2.cvtColor (cannyEdges, cv2.COLOR_HSV2BGR)

th, thresh = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
th, thresh_inverted = cv2.threshold(src, 80, 255, cv2.THRESH_BINARY_INV)
edges= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
edges2= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 9, 10)

color = cv2.bilateralFilter (src, 2, 300, 300)
# color = cv2.stylization(color, sigma_s=200, sigma_r=0.10)  

thresh =cv2.cvtColor (thresh, cv2.COLOR_BGR2GRAY)
thresh_inverted= cv2.cvtColor (thresh_inverted, cv2.COLOR_BGR2GRAY)
dst = cv2.Laplacian(src, ddepth, ksize=kernel_size)

# converting back to uint8
abs_dst = cv2.convertScaleAbs(dst)
laplacian =cv2.cvtColor (abs_dst, cv2.COLOR_BGR2GRAY)

#imgmask = np.uint8(dst)
cartoon = cv2.bitwise_and (laplacian, laplacian, mask= edges )
cartoon2 = cv2.bitwise_and (color, color, mask= cannyEdges )
cartoon3 = cv2.bitwise_and (color, color, mask= laplacian )
cartoon4 = cv2.bitwise_and (color, color, mask= thresh)
cartoon5 = cv2.bitwise_and (thresh_inverted, thresh_inverted, mask= gray)


gamma =2

lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
cartoon2 = cv2.LUT(cartoon2, lookUpTable)

cv2.imshow("cartoon", cartoon)
cv2.imshow("cartoon2", cartoon2)
cv2.imshow("cartoon3", cartoon3)
cv2.imshow("cartoon4", cartoon4)
cv2.imshow("cartoon5", cartoon5)
# cv2.imshow("thresh", thresh)
# cv2.imshow ("edges", edges)
# cv2.imshow("laplacian", abs_dst )

cv2.waitKey(0) 
   