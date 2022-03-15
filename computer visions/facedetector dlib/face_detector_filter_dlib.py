import cv2
import dlib
import numpy as np
from dataPath import DATA_PATH
import os

glasses =  DATA_PATH + "/images/lenses"
faceImagePath = DATA_PATH + "/images/picture.jpg"
mustacheImagePath =  DATA_PATH + "/images/mustache.png"
saveImagePath = DATA_PATH + "/images/imagefilter.jpg"
lensReflexions = DATA_PATH + "/images/city.jpg"
modelPath = DATA_PATH + "models/shape_predictor_68_face_landmarks.dat"

webcam = False
cap = cv2.VideoCapture(0)

# create object instance of detector and predictor using dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(modelPath)


def trackbar (n):
    pass

cv2.namedWindow ("filter")
cv2.resizeWindow("filter", 640, 480)

cv2.createTrackbar ("bluelips", "filter", 0 ,255, trackbar)
cv2.createTrackbar ("greenlips","filter", 0, 255, trackbar)
cv2.createTrackbar ("redlips",  "filter", 0, 255, trackbar)

cv2.createTrackbar ("blueeye", "filter", 0, 255, trackbar)
cv2.createTrackbar ("greeneye","filter", 0, 255, trackbar)
cv2.createTrackbar ("redeye",  "filter", 0, 255, trackbar)

cv2.createTrackbar ("lenses","filter", 0, 6, trackbar )

cv2.createTrackbar ("mustache","filter", 0, 1, trackbar )
cv2.createTrackbar ("saveimage","filter", 0, 1, trackbar)


def facelandmarks (faces):

    myFacePoints= []

    for face in faces:
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        # imgOriginal = cv2.rectangle(img, (x1, y1),(x2, y2), (0,255,0),2)
        landmarks = predictor (imgGray, face)
        
        for n in range (68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            myFacePoints.append ([x,y])
            # cv2.circle (imgOriginal, (x,y), 5, (50,50,255), cv2.FILLED)
            # cv2.putText(imgOriginal, str(n), (x,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1)
            # cv2.imshow ("text", imgOriginal)
      
        # cv2.imshow ("filter", imgOriginal)
        # print (myFacePoints)
        return myFacePoints

# create a mask or crop to get an specify image area using keypoints detector
def createBox (img, points, scale = 5, masked = False, cropped = True):
    points = np.array (points)

    if masked:
        mask = np.zeros_like(img)
        mask = cv2.fillPoly(mask, [points], (255,255, 255))
        img = cv2.bitwise_and(img, mask)
        # cv2.imshow("mask", img)

    if cropped:
        bbox= cv2.boundingRect(points)
        x,y,w,h = bbox
        imgCrop = img[y: y+h, x:x+w]
        imgCrop = cv2.resize (imgCrop, (0,0), None, scale, scale)
        return imgCrop
    else:
        return mask

# load images of glasses and return it as a list.
def load_images_from_folder(glasses):
    images = []
    for filename in os.listdir(glasses):
        img = cv2.imread(os.path.join(glasses,filename), -1)
        if img is not None:
            images.append(img)
    return images

# save new image with final filter.
def saveImage (path, data):
    folder = path
    image = data
    imageWrite = cv2.imwrite(folder, image)
    saveData = cv2.getTrackbarPos ("savedata", "filter")
    if saveData:
         imageWrite = cv2.imwrite(folder, image)
        #  cv2.imshow ("imageWrite", imageWrite)       
    else :
        pass

# getting lefteye area, and filter with color    
def leftEye (facePoints, img):

    facePoints = np.array (facePoints)
    imgLeftEye= createBox(img, facePoints [36:42],3, masked= True, cropped= False)
    imgColorLeftEye= np.zeros_like (imgLeftEye)
    blueEye = cv2.getTrackbarPos ("blueeye", "filter")
    greenEye = cv2.getTrackbarPos ("greeneye", "filter")
    redEye = cv2.getTrackbarPos ("redeye", "filter")
    imgColorLeftEye[:]= blueEye, greenEye, redEye
    imgColorLeftEye = cv2.bitwise_and(imgLeftEye, imgColorLeftEye)
    imgColorLeftEye = cv2.GaussianBlur (imgColorLeftEye, (7,7), 10)
    return imgColorLeftEye

# getting rightEye area, and filter with color 
def rightEye (facePoints, img):

    facePoints = np.array (facePoints)
    imgRightEye = createBox (img , facePoints[43:48],3, masked= True, cropped= False )
    imgColorRightEye= np.zeros_like (imgRightEye)

    blueEye = cv2.getTrackbarPos ("blueeye", "filter")
    greenEye = cv2.getTrackbarPos ("greeneye", "filter")
    redEye = cv2.getTrackbarPos ("redeye", "filter")
    imgColorRightEye[:]= blueEye, greenEye, redEye
    imgColorRightEye = cv2.bitwise_and(imgRightEye, imgColorRightEye)
    imgColorRightEye = cv2.GaussianBlur (imgColorRightEye, (7,7), 10)
    return imgColorRightEye

# getting lips area, and filter with color    
def colorLips (facePoints, img):
    
    facePoints = np.array (facePoints)
    imgLips = createBox(img, facePoints [48:61],3, masked= True, cropped= False)
    imgColorLips= np.zeros_like (imgLips)
    b = cv2.getTrackbarPos ("bluelips", "filter")
    g = cv2.getTrackbarPos ("greenlips","filter")
    r = cv2.getTrackbarPos ("redlips",  "filter")
    imgColorLips[:]= b, g, r
    imgColorLips = cv2.bitwise_and(imgLips, imgColorLips)
    imgColorLips = cv2.GaussianBlur (imgColorLips, (7,7), 10)
    return imgColorLips


# adding mustache to face    
def mustache (facePoints, image):
    
    facePoints = np.array (facePoints)
    imgMustache = image
    # mustache mask
    mustacheMask = imgMustache[:,:,3]

    #inverted mustache mask
    mustacheMaskIinv = cv2.bitwise_not(mustacheMask)

    imgMustache = imgMustache[:,:,0:3]

    # get image mustache size
    origMustacheHeight, origMustacheWidth = mustacheMask.shape[:2]
    
    # get facial landmarks normalize
    mustacheWidth = abs(facePoints[31][0] - facePoints[1][0])
      
    # get image mustache height roi area 
    mustacheHeight = int( mustacheWidth *  origMustacheHeight / origMustacheWidth)

    # rezise mustache image
    mustache = cv2.resize(imgMustache, (mustacheWidth, mustacheHeight), interpolation = cv2.INTER_AREA)
    
   # mask
    mask = cv2.resize(mustacheMask, (mustacheWidth, mustacheHeight), interpolation = cv2.INTER_AREA)
    maskInverse =cv2.resize(mustacheMaskIinv, (mustacheWidth, mustacheHeight), interpolation = cv2.INTER_AREA)
    
    y1 = int(facePoints[33][1])
    y2 = int(y1 + mustacheHeight)
    x1 = int(facePoints[51][0] - (mustacheWidth/2))
    x2 = int(x1 + mustacheWidth)
    
    regionOfInterest = img[y1:y2, x1:x2]
    regionOfInterestBackground = cv2.bitwise_and(regionOfInterest,regionOfInterest, mask = maskInverse)
    regionOfInterestForeground = cv2.bitwise_and(mustache, mustache,mask = mask)
      
    # condition to get trackbar position and show effect
    mustacheTrackbar = cv2.getTrackbarPos ("mustache", "filter")
    if mustacheTrackbar:
        imgOriginal[y1:y2, x1:x2] = cv2.add(regionOfInterestBackground, regionOfInterestForeground)
        # cv2.imshow ("filter", imgOriginal)
        return
    else :
        pass
     
# adding glasses to face      
def glassesEffect (facePoints, image, reflexions = True):

    facePoints = np.array (facePoints)
    imgGlass = image
    imgGlass =imgGlass 
    #glass mask
    glassMask = imgGlass[:,:,3]
    # cv2.imshow ("glassmask", glassMask)
    # imgGlass = cv2.cvtColor(imgGlass,cv2.COLOR_BGR2RGB)
    # imGlass = imgGlass.shape
    # print("Rows of Pixels: %d Rows"%(imGlass[0]))
    # print("Columns of Pixels: %d Columns"%(imGlass[1]))
    # print("Color Channels: %d Color Channels"%(imGlass[2]))    glassMask = imgGlass[:,:,3]

    #inverted glass mask
    glassMaskIinv = cv2.bitwise_not(glassMask)
    # cv2.imshow ("inverted glassmask", glassMaskIinv)
    imgGlass = imgGlass[:,:,0:3]
    # cv2.imshow ("imgGlass", imgGlass)

    # get image glass size
    origGlassHeight, origGlassWidth = imgGlass.shape[:2]
    
    # get facial landmarks normalize
    glassWidth = abs(facePoints[16][0] - facePoints[1][0])
      
    # get image glass height roi area 
    glassHeight = int(glassWidth * origGlassHeight / origGlassWidth)

    # rezise glass image
    glass = cv2.resize(imgGlass, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
    
   # mask
    mask = cv2.resize(glassMask, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
    maskInverse =cv2.resize(glassMaskIinv, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
    
    #assign facepoints to region of interest
    y1 = int(facePoints[24][1])
    y2 = int(y1 + glassHeight)
    x1 = int(facePoints[27][0] - (glassWidth/2))
    x2 = int(x1 + glassWidth)
    
    regionOfInterest = img[y1:y2, x1:x2]
    regionOfInterestBackground = cv2.bitwise_and(regionOfInterest,regionOfInterest, mask = maskInverse)
    regionOfInterestForeground = cv2.bitwise_and(glass, glass,mask = mask)
    if reflexions:
        #adding glass reflexion
        glassReflexion = cv2.imread (lensReflexions)
        glassReflexion = glassReflexion[:,:,0:3]
        ReflexionMask = cv2.resize(glassReflexion, (glassWidth,glassHeight), interpolation = cv2.INTER_AREA)
        roiReflexion = cv2.bitwise_and (ReflexionMask, ReflexionMask, mask = mask)
        regionOfInterestForeground = cv2.addWeighted (regionOfInterestForeground, 1, roiReflexion, 0.7, 0)
        # cv2.imshow ("lensreflexion", roiReflexion)
    else :
        pass

    # condition to get trackbar position and show effect
    lenses = cv2.getTrackbarPos ("lenses", "filter")
    if lenses:
        imgOriginal[y1:y2, x1:x2] = cv2.add(regionOfInterestBackground, regionOfInterestForeground)
        cv2.imshow ("filter", imgOriginal)
        return
    else :
        pass

while True:

#reading source image, or webcam
    if webcam: success, img = cap.read ()
    else:
        img = cv2.imread (faceImagePath)

#creating an image copy, and converte it to grayscale
    imgOriginal = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#calling face detector
    faces = detector(imgGray)
    facePoints = facelandmarks (faces)

#calling funtions
    imgGlass = load_images_from_folder(glasses)
# dt = np.dtype(np.uint8)

    imgMustache = cv2.imread (mustacheImagePath, -1)
    
    imgGlasses = np.array(imgGlass)     
# imgGlass=np.uint8(imgGlass)
        
# get Trackbar position of lenses to change images of glasses
    pos = cv2.getTrackbarPos("lenses", "filter")


# if position is equal 0, return Blank image     
    if pos == 0:
# size of the image
        (H , W) = 200, 200
# Blank image with RGBA = (0, 0, 0, 0)
        imgGlasses = np.full((H, W, 4), (0, 0, 0, 0), np.uint8)

# if position is equal 1, return firts image        
    elif pos == 1:
        imgGlasses = imgGlasses[0]

    elif pos == 2:
        imgGlasses = imgGlasses[1]
   
    elif pos == 3:
        imgGlasses = imgGlasses[2]
            
    elif pos == 4:
        imgGlasses = imgGlasses[4]

    elif pos == 5:
        imgGlasses = imgGlasses[5]

    elif pos == 6:
        imgGlasses = imgGlasses[6]
    
# calling functions 
    lefEyeEffect =  leftEye(facePoints, img)
    rightEyeEffect = rightEye(facePoints, img)
    lipsEffect = colorLips (facePoints, img)
    glassEffect = glassesEffect (facePoints, imgGlasses)
    mustacheEffect = mustache (facePoints, imgMustache)

# blending image return from functions.
    faceEffect = cv2.addWeighted (lefEyeEffect, 1, rightEyeEffect, 1, 0)
    faceEffect = cv2.addWeighted (lipsEffect, 1, faceEffect, 1, 0)
    faceEffect = cv2.add (imgOriginal, faceEffect) 
    saveImage (saveImagePath, faceEffect)

# show final effect, and image with trackbar. 
    cv2.imshow ("final", faceEffect)
    cv2.imshow ("filter", faceEffect)

# press q key to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
            break









