import json
import cv2
import numpy as np
import base64
with open('cam.json','r') as f:
  d = json.load(f)
print(d)
for i in d:
  x = d[i]
  # print("value:",i["cam"])
cap = cv2.VideoCapture(x)
while True:
  ret,frame = cap.read()
  cv2.imshow("frame",frame)
  if cv2.waitKey(1) and 0xFF==ord('q'):
    break
cap.release()

