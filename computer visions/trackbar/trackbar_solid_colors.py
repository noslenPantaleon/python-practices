import numpy as np
import cv2 as cv


def function (x):
    # cv.GaussianBlur()
    print (x)

img = np.zeros ((300, 512, 3), np.uint8)
# image = cv.imread ("../data/images/sample.png", 0)
# # Convert unsigned int to float
# img = np.float32(image)

cv.namedWindow ("image")

cv.createTrackbar ("B", "image", 0, 255, function)
cv.createTrackbar ("G", "image", 0, 255, function)
cv.createTrackbar ("R", "image", 0, 255, function)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, function)

while (1):
    cv.imshow ("image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos ("B", "image")
    g = cv.getTrackbarPos ("G", "image")
    r = cv.getTrackbarPos ("R", "image")
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       img[:] = 0
    else:
       img[:] = [b, g, r]

cv.destroyAllWindows()

# cv2.imshow("Image blue",img[:,:,0])
# cv2.imshow("Image green",img[:,:,1])
# cv2.imshow("Image red",img[:,:,2])

    # cv2.imshow(windowName, scaledImage)

    # img [:] = [b, g, r]


# if s == 0
#     pass
# else:
#     img = cv.cvtColor()
#     img [:]= 0







# pos = cv.getTrackbarPos ("CP", "image")
#     font = cv2.FONT_HERSHEY_COMPLEX
#     cv.putText (img, str(pos), (50, 150), font, 4, (0, 0, 255))