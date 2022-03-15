import numpy as np
import cv2 


windowName = "mouse interaction"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

emptyMatrix = np.zeros((100,200,3),dtype='uint8')
maxScaleUp = 100
scaleValue = 20
scaleType = 0
maxType = 1
scalingFactor = 1.0


def resizeImage(action, x, y, flag, userdata):
  # Referencing global variables 
  global scalingFactor, scalingType

  # if (action == [cv2.EVENT_MOUSEWHEEL]) and (flag & [cv2.EVENT_FLAG_CTRLKEY]):
  if (action == cv2.EVENT_MOUSEWHEEL and cv2.EVENT_FLAG_CTRLKEY):
    # print (action, flag)
    
    # Action to be taken when ctrl key + mouse wheel scrolled forward
    if (flag > 0):
      # Resize image
      print ("rezise image")
      scalingFactor = 1 - scaleValue/100.0 
      scaledImageUp = cv2.resize(emptyMatrix, None, fx =scalingFactor,\
              fy = scalingFactor, interpolation = cv2.INTER_LINEAR)
      cv2.imshow(windowName, scaledImageUp)
     
   
    # Action to be taken when ctrl key + mouse wheel scrolled backward
    else:
      # Resize image
      scalingFactor = 1 + scaleValue/100.0
      print (" not rezise image")
      scaledImageDown = cv2.resize(emptyMatrix, None, fx=scalingFactor,\
              fy = scalingFactor, interpolation = cv2.INTER_LINEAR)
      cv2.imshow(windowName, scaledImageDown)
    

  
cv2.setMouseCallback (windowName, resizeImage)


while True:  
  c = cv2.waitKey(10)
  if c==27:
      break

cv2.destroyAllWindows()