import cv2
import numpy as np

# load image with alpha channel
img = cv2.imread("../data/images/picture.jpg", cv2.IMREAD_UNCHANGED)

# extract alpha channel
alpha = img[:,:,2]

# extract bgr channels
bgr = img[:,:,0:3]

# convert to HSV
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
#h = hsv[:,:,0]
#s = hsv[:,:,1]
#v = hsv[:,:,2]
h,s,v = cv2.split(hsv)

# purple is 276 in range 0 to 360; so half in OpenCV
# green is 120 in range 0 to 360; so half in OpenCV
purple = 138
green = 60

# diff color (green - hue)
diff_color = green - purple

# modify hue channel by adding difference and modulo 180
hnew = np.mod(h + diff_color, 180).astype(np.uint8)

# recombine channels
hsv_new = cv2.merge([hnew,s,v])

# convert back to bgr
bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)

# put alpha back into bgr_new
bgra = cv2.cvtColor(bgr_new, cv2.COLOR_BGR2BGRA)
bgra[:,:,3] = alpha

# save output
cv2.imwrite('sword_alpha.png', alpha)
cv2.imwrite('sword_bgr.png', bgr)
cv2.imwrite('sword_bgr_new.png', bgr_new)
cv2.imwrite('sword_green.png', bgra)

# Display various images to see the steps
cv2.imshow('alpha',alpha)
cv2.imshow('bgr',bgr)
cv2.imshow('bgr_new',bgr_new)
cv2.imshow('bgra',bgra)
cv2.waitKey(0)
cv2.destroyAllWindows()