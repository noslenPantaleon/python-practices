import cv2
import numpy as np
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print (events)

class MousePts:
    def __init__(self,windowname,img):
        self.windowname = windowname
        self.img1 = img.copy()
        self.img = self.img1.copy()
        cv2.namedWindow(windowname,cv2.WINDOW_NORMAL)
        cv2.imshow(windowname,img)
        self.curr_pt = []
        self.point   = []

    def select_point(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point.append([x,y])
            #print(self.point)
            cv2.circle(self.img,(x,y),5,(0,255,0),-1)
        elif event == cv2.EVENT_MOUSEMOVE:
            self.curr_pt = [x,y]
            #print(self.point)
                   
    def getpt(self,count=1,img=None):
        if img is not None:
            self.img = img
        else:
            self.img = self.img1.copy()
        cv2.namedWindow(self.windowname,cv2.WINDOW_NORMAL)
        cv2.imshow(self.windowname,self.img)
        cv2.setMouseCallback(self.windowname,self.select_point)
        self.point = []
        while(1):
            cv2.imshow(self.windowname,self.img)
            k = cv2.waitKey(20) & 0xFF
            if k == 27 or len(self.point)>=count:
                break
            #print(self.point)
        cv2.setMouseCallback(self.windowname, lambda *args : None)
        #cv2.destroyAllWindows()
        return self.point, self.img
         
if __name__=='__main__':
    img = np.zeros((512,512,3), np.uint8)
    windowname = 'image'
    coordinateStore = MousePts(windowname,img)

    pts,img = coordinateStore.getpt(3)
    print(pts)
        
    pts,img = coordinateStore.getpt(3,img)
    print(pts)
    
    cv2.imshow(windowname,img)
    cv2.waitKey(0)