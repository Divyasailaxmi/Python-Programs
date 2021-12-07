import cv2
from commonutils import *
import json
import numpy as np
import base64
with open("/home/divya/Desktop/Divya/cam.json",'r') as f:
  d = json.load(f)
while True:  
  for i in d:
    print("Value: ",i['cam_id'])
  cap = cv2.VideoCapture(i['cam_id'])
  ret,frame = cap.read()
  cache = CacheHelper()
  cache.set_json({"value"+str(i["cam_id"]): frame})
  if cv2.waitKey(50) ==ord('q'):
      break
cap.release()


# with open("/home/divya/Desktop/Divya/cam.json",'r') as f:
#   d = json.load(f)
# print(d)
# li=[]
# for i in d:
#   print("Value:",i)
#   cap = cv2.VideoCapture(d[i])
# # while True:
#   ret,frame = cap.read()
#   cache = CacheHelper()
#   cache.set_json({"vid": frame})
#   cv2.imshow("frame"+i,frame)
#   cv2.imwrite("frame"+i+".jpg",frame)
#   print("frame"+i+".jpg")
#   li.append("frame"+i+".jpg")
#   if cv2.waitKey(1) ==ord('q'):
#       break
# print(li)      
# cap.release()
# cv2.destroyAllWindows()




# define a video capture object
# vid = cv2.VideoCapture(0)
# if (vid.isOpened() == False): 
#     print("Error reading video file")
# frame_width = int(vid.get(3))
# frame_height = int(vid.get(4))
# res = cv2.VideoWriter('vid.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
# while(True):
#     ret, frame = vid.read()
#     cache = CacheHelper()
#     cache.set_json({"vid": frame})
#     res = cv2.VideoWriter("video7.avi",cv2.VideoWriter_fourcc(*'mp4V'),15,(frame_width,frame_height))   
#     res.write(frame)
#     # cv2.imwrite("out.Jpg",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# res.release()
# cv2.destroyAllWindows()




