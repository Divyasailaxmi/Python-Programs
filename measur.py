from scipy.spatial import distance as dist
#from imutils import perspective
#from imutils import contours
import numpy as np
import argparse
#import imutils
import cv2
#from google.colab.patches import cv2_imshow
img = cv2.imread('/content/drive/MyDrive/dd715.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(img, (7, 7), 0)
edged = cv2.Canny(img, 50, 100)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
for cnt in cnts:
  rect = cv2.minAreaRect(cnt)
  (x,y),(w,h),angle = rect
  box = cv2.boxPoints(rect)
  box = np.int0(box)
  cv2.polylines(img,[box],True,(255,0,0),2)
  cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1)
  cv2.putText(img,'width{}'.format(round(w,1),(int(x),int(y-15)),cv2.FONT_HERSHEY_PLAIN),2,(100,200,0),2)
  cv2.putText(img,'Height{}'.format(round(h,1),(int(x),int(y+15)),cv2.FONT_HERSHEY_PLAIN),2,(100,200,0),2)
cv2.imshow("image",img)