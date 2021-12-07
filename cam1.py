import json
import cv2
import numpy as np
import base64

with open("/home/divya/Desktop/Divya/cam.json",'r') as f:
  d = json.load(f)
while True:      
  for i in d:
      print("Value: ",i['cam_id'])   
      cap = cv2.VideoCapture(i['cam_id'])
  # while True:    
      ret,frame = cap.read()
      cv2.imshow("frame"+str(i['cam_id'])+".jpg",frame)
      cv2.imwrite("frame"+str(i['cam_id'])+".jpg",frame)
      # print("frame"+i+".jpg")
      # li.append("frame"+i+".jpg")
      if cv2.waitKey(500) ==ord('q'):
        break
  # while True:
      # cv2.imshow('frame3',frame3)
      # cv2.imshow("frame"+str(i)+".jpg",frame)
      # print("frame"+i+".jpg")
      # li.append("frame"+i+".jpg")
      # if cv2.waitKey(0) ==ord('q'):
      #     break
    # print(li)    
  cap.release()
  cv2.destroyAllWindows()
