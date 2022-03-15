import cv2
import numpy as np
from dataPath import DATA_PATH



# Read an image in grayscale
imagePath = DATA_PATH + '/images/picture.jpg'
src = cv2.imread(imagePath, 1)
   
def dodgeV2(image, mask):
        return cv2.divide(image, 255-mask, scale=256)

def renderv2(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, (21,21), 0, 0)
    img_blend = dodgeV2(img_gray, img_blur)
    img_blend = cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)
    return cv2.imshow ("renderV2", img_blend)


def renderv1(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21,21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)
    return cv2.imshow ("renderV1", img_blend)

renderv1 (src)
renderv2 (src)
cv2.waitKey(0) 
