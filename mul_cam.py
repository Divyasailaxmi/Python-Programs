import cv2
import json

fr = open('cam.json')
data = json.load(fr)
fr.close()


vids = [cv2.VideoCapture(i["cam_id"]) for i in data]


while True:
    all_frames = []

    for i in vids:
        ret,frame = i.read()
        all_frames.append(frame)
    
    for c,f in enumerate(all_frames):
        cv2.imshow(str(c),all_frames[c])

        cv2.waitKey(1)



