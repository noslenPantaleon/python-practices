import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('color', frame)
    cv2.imshow('grey', gray)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.show()

    if (cv2.waitKey(1) & 0xFF == 27):
        break



cap.release()
cv2.destroyAllWindows()
