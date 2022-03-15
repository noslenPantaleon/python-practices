import cv2
import numpy as np

maxScaleUp = 100
scaleValue = 1
scaleType = 0
maxType = 1
scaleFactor = 1.0
windowName = "Resize Image"
trackbarValue = "Scale"
trackbarRotation = "Rotation"
trackbarSharpen= "sharpen image"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"
trackbarcolorpixels= "Color Numbers pixels"
scalevalues= "scale porcentage"
trackbarColor2gray = 'color/gray'
trackbarBlueChannel="blue channel"
trackbarGreenChannel="green channel"
trackbarRedChannel="red channel"
scale = ()

# load an image
img = cv2.imread("../data/images/microgreen.jpg")



# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleTypeImage(*args):

    global scaleType
    global scaleValue
    global scaleFactor

    scaleType = args[0]
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    else:
        scaleFactor = 1 + scaleValue/100.0
    if scaleFactor == 0 :
        scaleFactor = 1
    scaledImage = cv2.resize(img, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

#funtion to scale image
def scaleImage(*args):

    global scaleValue
    global scaleType
    global scaleFactor

    scaleValue = args[0]
    if scaleType == 1:
        scaleFactor = 1 - scaleValue/100.0
    else:
        scaleFactor = 1 + scaleValue/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(img, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

#funtion to rotated image
def imagerotation(*args):

    global rotation

    rows,cols, ch = img.shape
    rotation = args[0]   
    rotatedImage = cv2.getRotationMatrix2D((cols/2,rows/2),rotation,1)
    dst = cv2.warpAffine(img, rotatedImage ,(cols,rows))
    cv2.imshow(windowName, dst)

#funtion to filter color gray 
def getcolorgraytrackbar (*args):
    
    global img

    colorgrayTrackbar = args[0]   
    if colorgrayTrackbar == 0:
        cv2.imshow(windowName, img)
        
    else:   
        imgProcess = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        cv2.imshow(windowName, imgProcess)

     
#funtion to sharpen an image
def sharpen (*args):

    global img
    trackbarsharpen = args[0]
    kernel3 = np.array([[0, -1,  0],

                    [-1,  5, -1],

                        [0, -1,  0]])

    if trackbarsharpen == 0:
        cv2.imshow(windowName, img)
        
    else:
        sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel3)
        cv2.imshow(windowName, sharp_img)

#funtion to get blue channel with color
def colorblue (*args):
    
    global img   
    trackbarbluechannel = args[0]
    if trackbarbluechannel == 0:
        cv2.imshow(windowName, img)
        
    else:
        # getting heith and width of the image with numpy
        blank= np.zeros (img.shape [:2], dtype= 'uint8')

        # split in channels the image
        b,g,r= cv2.split(img)

        # merge in channels the image
        blue= cv2.merge ([b, blank, blank ])
        cv2.imshow(windowName, blue)


#funtion to get red channel with color
def colorred (*args):
    
    global img   
    trackbarredchannel = args[0]
    if trackbarredchannel == 0:
        cv2.imshow(windowName, img)
        
    else:
        # getting heith and width of the image with numpy
        blank= np.zeros (img.shape [:2], dtype= 'uint8')

        # split in channels the image
        b,g,r= cv2.split(img)

        # merge in channels the image
        red= cv2.merge ([blank, blank, r]) 
        cv2.imshow(windowName, red)

  
#funtion to get green channel with color
def colorgreen (*args):
    
    global img   
    trackbargreenchannel = args[0]
    if   trackbargreenchannel == 0:
        cv2.imshow(windowName, img)
        
    else:
        # getting heith and width of the image with numpy
        blank= np.zeros (img.shape [:2], dtype= 'uint8')

        # split in channels the image
        b,g,r= cv2.split(img)

        # merge in channels the image
        green= cv2.merge ([blank, g, blank])
        cv2.imshow(windowName, green)

 #Create trackbar controllers

cv2.createTrackbar(trackbarValue, windowName, scaleValue, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)
cv2.createTrackbar(trackbarRotation, windowName, 0, 360, imagerotation)
cv2.createTrackbar(trackbarColor2gray, windowName, 0, 1, getcolorgraytrackbar)
cv2.createTrackbar(trackbarSharpen, windowName, 0, 1, sharpen)
cv2.createTrackbar(trackbarBlueChannel, windowName, 0, 1, colorblue)
cv2.createTrackbar(trackbarRedChannel, windowName, 0, 1, colorred)
cv2.createTrackbar(trackbarGreenChannel, windowName, 0, 1, colorgreen)

#get  trackbar positions
trackbargray = cv2.getTrackbarPos(trackbarColor2gray, windowName)
trackbarbluechannel = cv2.getTrackbarPos(trackbarBlueChannel, windowName)
trackbarredchannel = cv2.getTrackbarPos(trackbarRedChannel, windowName)
trackbargreenchannel = cv2.getTrackbarPos(trackbarGreenChannel, windowName)
trackbarRotated = cv2.getTrackbarPos (trackbarRotation, windowName)

imagerotation (trackbarRotated) 



while True:  
    c = cv2.waitKey(10)
    if c==27:
        break

cv2.destroyAllWindows()