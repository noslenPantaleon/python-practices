import cv2
import os
from dataPath import DATA_PATH

folder = DATA_PATH + "/images/"

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


images = load_images_from_folder(folder)
# print (images)

for i, img in enumerate (images):
    cv2.imshow("Image number {}".format(i), img)



cv2.waitKey(0)