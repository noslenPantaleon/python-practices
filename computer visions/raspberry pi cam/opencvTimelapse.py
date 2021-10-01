
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import datetime
import cv2

import sys
import os


cam = PiCamera()
rawCapture = PiRGBArray(cam)
cam.capture(rawCapture, format="bgr")
image = rawCapture.array
cam.resolution = (1920, 1080)
time.sleep(0.1)







i = 0

while True:
     now = datetime.datetime.now()
     hs = now.hour
     print (hs)
     dia=12
     noche=0



     if (hs<dia):

               global i
               i = i + 1
               cam.capture('/home/shares/public/microgreennoche_%s.jpg' % i)
               print ("camara noche")
               time.sleep(60)


     else:


               global i
               i = i + 1
               cam.exposure_mode = "off"
               cam.shutter_speed =10000 # microsecon
               cam.brightness= 42


               cam.capture('/home/shares/public/microgreendia_%s.jpg' % i)
               print ("camara dia")
               time.sleep(60)











cv2.waitKey(0)
