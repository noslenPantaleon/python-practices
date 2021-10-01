
# import our libraries
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
import datetime
import sys
import os


# variables frames
frames_dia= 1080
frames_noche=360

cam_dia= 9
cam_noche= 3


# detecta la hora exacta

now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)


# set up our camera
cam = PiCamera()
rawCapture = PiRGBArray(cam)
cam.resolution = (1920, 1080)
time.sleep(0.1)



# grab an image from the camera
cam.capture(rawCapture, format="bgr")
image = rawCapture.array




def camera_noche():

    while (now.hour>=cam_noche ):


        for i in range(frames_noche):
            cam.capture('/home/shares/public/plant{0:07d}.jpg'.format(i))
            time.sleep(60)
            print ("camara noche")






def camera_dia():
     while (now.hour>=cam_dia ):

        for i in range(frames_dia):
            os.system("fswebcam -i 0 -d /dev/video0 -r 1920x1080 -p YUYV -q --title @Noslen /home/shares/public/webcam/%d%$
            time.sleep(60)
            print ("camara dia")
            
            
            


camera_dia()
camera_noche()

            
