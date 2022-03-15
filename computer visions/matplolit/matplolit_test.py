import cv2
from matplotlib import pyplot as plt
import numpy as np
from dataPath import DATA_PATH

imagePath = DATA_PATH + "/images/picture.jpg"
img = cv2.imread(imagePath, -1)
cv2.imshow("Display Image", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

while True:
    c = cv2.waitKey(20)
    if c == 27:
        break

cv2.destroyAllWindows()