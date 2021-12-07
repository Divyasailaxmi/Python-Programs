import cv2
import threading
from kafka import KafkaProducer
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
    def set_json(self, dict_obj):
        try:
            k, v = list(dict_obj.items())[0]
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


def preprocess_image(frame, preprocess):
    for p in preprocess:
        if p == 'rotate_180':
            frame = cv2.rotate(frame, cv2.ROTATE_180)
        if p == 'rotate_90':
            frame = cv2.rotate(frame, cv2.ROTATE_90)
    return frame


def camPreview(previewName, camID, preprocess=[]):
    print("previewName-------",previewName)
    topic = str(camID)
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda value: json.dumps(value).encode(), )
    
    
    print("toipc",topic)
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    print(camID)
    if cam.isOpened():
        rval, frame = cam.read()
            
    else:
        rval = False

    while rval:
        rval, frame = cam.read()
        if preprocess and len(preprocess) > 0:
            frame = preprocess_image(frame, preprocess)
        frame = cv2.resize(frame,(640,480))
        cv2.imshow(previewName,frame)
        # img = "temp.jpg"
        img = str(ObjectId()) + '.jpg'
        cv2.imwrite(img, frame)
        
        with open(img, 'rb') as f:
            im_b64 = base64.b64encode(f.read())
        payload_video_frame = {"frame": str(im_b64)}
        # print("payload_video_frame---------",payload_video_frame)
        future = producer.send(topic, value=payload_video_frame)
        print("topic",topic)
        CacheHelper().set_json({"topic" : payload_video_frame}) 
        os.remove(img)   
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()        
    # cv2.destroyAllWindows()


def __main__():
# Create threads as follows
    thread_pool = {}  
    

    # with open('config.json', 'r') as f:
    #     distros_dict = json.load(f)
    # if len(sys.argv) >1:
    #     if sys.argv[1] == '-a':
    #         f = open('config.json', 'r')
    #     elif sys.argv[1] == '-b':
    #         f = open('config1.json', 'r')
    #     else:
    #         print('The arguments to be given are either "-a" or "-b"')
    #         sys.exit(0)
    # else:
    #     print('Provide an argument')
    #     sys.exit(0)
    
    f = open('config.json', 'r')

    distros_dict = json.load(f)
    f.close()
    #print("Following Camera IDs will be used : ")
    # #print("heyyyyyyyy")
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
    