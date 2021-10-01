import numpy as np
import cv2
import time

# time delay between frames
delay = 10

# folder to write to
folder = ''

camera = cv2.VideoCapture(0)
# 2304 x 1296 gets me 1280x720
camera.set(4, 2304.0)
camera.set(3, 1296.0)
#print str(camera.get(3)),str(camera.get(4))

ret, frame = camera.read()
count = 0
while(1):
    ret, frame = camera.read()
    frame_number = "%08d" % (count,)
    cv2.imwrite(folder + frame_number + '.jpg', frame)
    k = cv2.waitKey(1)
    count = count + 1
    time.sleep(delay)

cv2.destroyAllWindows()
camera.release()