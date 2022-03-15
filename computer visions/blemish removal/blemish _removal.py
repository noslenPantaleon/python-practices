import cv2
import numpy as np
from dataPath import DATA_PATH

#list to store the points
r= 15
i = 0

# img =  DATA_PATH + "/images/lenses"
source = cv2.imread(DATA_PATH + "/images/blemish_1.jpg", 1)
dummy= source.copy()
cv2.namedWindow("Blemish Removal App")


# recieve data from mouse event funtion and
# crop the selected blemish.

def selectedBlemish (x,y,r):
    global i
    crop_im = source [y:(y+2*r), x: (x+2*r)]
    return indentifybestPatch (x,y,r)

# create dictionaty to save data collected from appendDictionary funtion
def indentifybestPatch (x,y,r):
    patches ={}
    key1tup = appendDictionary (x+2*r, y)
    patches ["key1"]= (x+2*r, y+r, key1tup [0], key1tup[1])
  
    key2tup = appendDictionary (x+2*r, y+r)
    patches ["key2"]= (x+2*r, y+r, key2tup [0], key2tup[1])

    key3tup = appendDictionary (x-2*r, y)
    patches ["key3"]= (x-2*r, y, key3tup [0], key3tup[1])
    
    key4tup = appendDictionary (x-2*r, y-r)
    patches ["key4"]= (x-2*r, y-r, key4tup [0], key4tup[1])

    key5tup = appendDictionary (x,y+2*r)
    patches ["key5"]= (x,y+2*r, key5tup [0], key5tup[1])

    key6tup = appendDictionary (x+r, y+2*r)
    patches ["key6"]= (x+r, y+2*r, key6tup [0], key6tup[1])

    key7tup = appendDictionary (x, y-2*r)
    patches ["key7"]= (x, y-2*r, key7tup [0], key7tup[1])

    key8tup = appendDictionary (x-r, y-2*r)
    patches ["key8"]= (x-r, y-2*r, key8tup [0], key8tup[1])

    # print patches
    print (patches)

#loop to find the minimal and maximun x and y values
    findlowx ={}
    findlowy = {}

    for key, (x, y, gx, gy) in patches.items ():
        findlowx [key]= gx

    for key, (x, y, gx, gy) in patches.items ():
        findlowy [key]= gy

    y_key_min = min(findlowy.keys(), key =(lambda k: findlowy [k]))
    x_key_min = min(findlowx.keys(), key =(lambda k: findlowx [k]))

    if x_key_min == y_key_min:
        return patches [x_key_min] [0], patches [x_key_min][1]

def appendDictionary (x,y):
    crop_img = source [y: (y+2*r), x:(x+2*r)]
    gradient_x, gradient_y = sobelfilter(crop_img)
    return gradient_x, gradient_y

def sobelfilter (crop_img):
    sobelx64f = cv2.Sobel (crop_img, cv2.CV_64F, 1,0, ksize=3)
    abs_xsobel64f= np.absolute (sobelx64f)
    sobel_x8u= np.uint8 (abs_xsobel64f)
    gradient_x = np.mean(sobel_x8u)

    sobely64f = cv2.Sobel (crop_img, cv2.CV_64F, 1,0, ksize=3)
    abs_ysobel64f= np.absolute (sobely64f)
    sobel_y8u= np.uint8 (abs_ysobel64f)
    gradient_y = np.mean(sobel_y8u)

    return gradient_x, gradient_y



def blemishRemoval (action, x, y, flags, userdata):
    global r, source
    #action to be taken whem left mouse button is pressed

    if action== cv2.EVENT_LBUTTONDOWN:
        # mark the center
        blemishLocation = (x,y)
        newX, newY= selectedBlemish(x,y,r)
        newPatch = source [newY:(newY+2*r), newX:(newX+2*r)]
        cv2.imwrite ("newpatch.png", newPatch)
       

        #create mask for the new patch
        mask = 255 * np.ones (newPatch.shape, newPatch.dtype)
        source= cv2.seamlessClone (newPatch, source, mask, blemishLocation, cv2.NORMAL_CLONE)
        cv2.imshow ("Blemish Removal App", source)

        #action to be taken when lef mouse button is released
    elif action== cv2.EVENT_LBUTTONUP:
        cv2.imshow ("Blemish Removal App", source)


cv2.setMouseCallback ("Blemish Removal App", blemishRemoval)
k= 0


while k!= 27:
    cv2.imshow ("Blemish Removal App", source)
    k = cv2.waitKey(20) & 0xFF
    if k== 99:
        source =dummy.copy()

cv2.destroyAllWindows ()






