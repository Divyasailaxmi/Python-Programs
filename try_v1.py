
  
import cv2
import numpy as np
# import json

# with open("/home/divya/Desktop/Divya/cam.json",'r') as f:
#   d = json.load(f) 


video1 = cv2.VideoCapture(0)
# video2 = cv2.VideoCapture('/home/divya/Desktop/Divya/4sec.mp4')

a = 1



while True:
    a = a +1    
        
    check1, frame1 = video1.read()
    # check2, frame2 = video2.read()
    cv2.imshow('Feed1',frame1 )
    # cv2.imshow('Feed2',frame2 )
    
    
    # saving video 
    # out.write(frame)
        
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
print(a)
video1.release()
# video2.release()
# out.release()

cv2.destroyAllWindows()