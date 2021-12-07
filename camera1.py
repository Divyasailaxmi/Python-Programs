############################
import cv2
import threading
# from kafka import KafkaProducer
import base64
import json
import numpy as np
import datetime
from bson import ObjectId
import os
import sys
import multiprocessing
import pickle
import redis

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class CacheHelper():
    def __init__(self):
        self.redis_cache = redis.StrictRedis(host="localhost", port="6379", db=0, socket_timeout=1)
        print("REDIS CACHE UP!")

    def get_redis_pipeline(self):
        return self.redis_cache.pipeline()
    
    #should be {'key'  : 'value'} always
    def set_json(self, k, v):
        try:
            #k, v = list(dict_obj.items())[0]
            v = pickle.dumps(v)
            return self.redis_cache.set(k, v)
        except redis.ConnectionError:
            return None

    def get_json(self, key):
        try:
            temp = self.redis_cache.get(key)
            #print(temp)\
            if temp:
                temp= pickle.loads(temp)
            return temp
        except redis.ConnectionError:
            return None
        return None

    def execute_pipe_commands(self, commands):
        #TBD to increase efficiency can chain commands for getting cache in one go
        return None


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting -----------" + self.previewName)
        self.camPreview(self.previewName, self.camID)


# def preprocess_image(frame, preprocess):
#     for p in preprocess:
#         if p == 'rotate_180':
#             frame = cv2.rotate(frame, cv2.ROTATE_180)
#         if p == 'rotate_90':
#             frame = cv2.rotate(frame, cv2.ROTATE_90)
#     return frame


def camPreview(previewName, camID, preprocess=[]):
    print("previewName-------",previewName)
    topic = str(camID)
    print("toipc",topic)
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(int(camID))
    print(type(camID))
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    print(rval)
    while True:
        rval, frame = cam.read()
        # if preprocess and len(preprocess) > 0:
        #    frame = preprocess_image(frame, preprocess)
        frame = cv2.resize(frame,(640,480))
        cv2.imshow(previewName,frame)
        # img = "temp.jpg"
        img = str(ObjectId()) + '.jpg'
        cv2.imwrite(img, frame)
        
        with open(img, 'rb') as f:
            im_b64 = base64.b64encode(f.read())
		#print(im_b64)
        payload_video_frame = {"frame": im_b64.decode("utf-8")}
        # print("payload_video_frame---------",payload_video_frame)
        # future = producer.send(topic, value=payload_video_frame)
        print("topic----------------",topic)
        if cv2.waitKey(33) == ord('a'):
            print ("topic sent pressed a--------------------------------------------------------") 
            CacheHelper().set_json(topic, payload_video_frame)

        print("came-----------------")
        os.remove(img)    
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()        
    cv2.destroyAllWindows()


def __main__():
# Create threads as follows
    thread_pool = {}  
    f = open('config.json', 'r')
    distros_dict = json.load(f)
    f.close()
    for distro in distros_dict:  
        if 'preprocess' not in distro:
            distro['preprocess'] = [] 
        thread_pool[distro['Camera_id']] = multiprocessing.Process(target=camPreview, args=(distro['camera_index'],distro['Camera_id'], distro['preprocess']))
        print()        
    for tt in thread_pool:
        thread_pool[tt].start()
    for tt in thread_pool:
        thread_pool[tt].join()
    
if __name__ == "__main__":
    __main__() 
    cv2.destroyAllWindows()
    
