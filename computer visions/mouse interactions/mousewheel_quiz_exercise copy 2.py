import cv2
import numpy as np
# Create a black image and a window
windowName = 'MouseCallback'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)
def CallBackFunc(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEWHEEL:
        print (event)
        # print("Left button of the mouse is clicked - position (", x, ", ",y, ")")
    
# bind the callback function to window
cv2.setMouseCallback(windowName, CallBackFunc)
def main():
    while (True):
        cv2.imshow(windowName, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()