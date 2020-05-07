#left click for selecting area on image
#right click to end the point selection process
#type "yes" on console after right click to see the result

import cv2
import numpy as np
#import  numpy

print("\n\nLeft click for selecting area on image\n right click to end the point selection process\n type 'yes' on console after right click to see the result")

img1=cv2.imread("pizza.jpg")
flag=0
xmax=0
xmin=0
ymax=0
ymin=0
img1=cv2.resize(img1,(512,512))
cv2.imshow("pizza", img1)
s=None
pts=[]

class points:
    x=None
    y=None
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def check(self,a,b):
        self.x=a
        self.y=b
        global flag
        global xmax
        global xmin
        global ymax
        global ymin
        if flag==0:
            xmax=self.x
            xmin=self.x
            ymax=self.y
            ymin=self.y
            flag=1
        else:
            if(self.x>xmax):
                xmax=self.x
                print('xmax is:')
                print(xmax)
            if(self.x<xmin):
                xmin=self.x
                print('xmin is:')
                print(xmin)
            if (self.y>ymax):
                ymax = self.y
                print('ymax is')
                print(ymax)
            if (self.y<ymin):
                ymin = self.y
                print('ymin is:')
                print(ymin)

def mouse(event,a,b,param,flags):
    if event==cv2.EVENT_LBUTTONDOWN:
        p=points(a,b)
        print('x point is:')
        print(a)
        print('y point is:')
        print(b)
        p.check(a,b)
        t=(a,b)
        pts.append(t)
        cv2.imshow("pizza", img1)
    if event==cv2.EVENT_RBUTTONDOWN:
        s = input('are you done ?')
        if s == 'yes':
            dx = abs(xmax-xmin)
            dy = abs(ymax-ymin)
            img2=np.zeros((512,512,3),np.uint8)
            imp = img1[ymin: ymax, xmin: xmax]
            img2[115:115 + dy, 115:115 + dx] = imp
            #img2[311:311 + dy, 294:294 + dx] = imp
            cv2.imshow("pizza", img2)

cv2.setMouseCallback("pizza",mouse)
cv2.waitKey(0)

