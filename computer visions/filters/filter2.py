import cv2
import numpy as np
from dataPath import DATA_PATH

# Read an image in grayscale
imagePath = DATA_PATH + '/images/picture.jpg'
image = cv2.imread(imagePath)

#convert to gray scale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#apply gaussian blur
grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
#detect edges
edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
edgeImage = 255 - edgeImage
#threshold image
ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)
#blur images heavily using edgePreservingFilter
edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)
#create output matrix
output =np.zeros(grayImage.shape)
#combine cartoon image and edges image
output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)
#Visualize the cartoon image 
cv2.imshow("Cartoon", output) 
cv2.waitKey(0) # "0" is Used to close the image window
cv2.destroyAllWindows()
