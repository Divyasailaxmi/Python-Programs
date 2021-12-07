

from inference_module import *
import glob
import torch.multiprocessing as multiprocessing
import redis

import cv2
import numpy as np
import io
import base64

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


def data_uri_to_cv2_img(encoded_string):
    #encoded_data = uri.split(',')[1]
    base64_image = str.encode(encoded_string)
    img = cv2.cvtColor(np.array(Image.open(io.BytesIO(base64.b64decode(base64_image)))), cv2.COLOR_BGR2RGB)
    #img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

#data_uri = "data:image/jpeg;base64,/9j/4AAQ..."
#img = data_uri_to_cv2_img(data_uri)
#cv2.imshow(img)

def cam(topic, idx):
    with torch.no_grad():
        predictor = Inference()       
        while True:
            frame = CacheHelper().get_json(topic)
            if frame:
                str_b64 = frame['frame']
                frame1 = data_uri_to_cv2_img(str_b64)
            #ret1,frame1 = cap1.read()


            
            t0 = datetime.now()

            predictor.input_frame  = frame1
            predicted_frame1, detector_predictions,cord  = predictor.dummy()
            cv2.imshow(topic+"_predicted",predicted_frame1)
            print("---------------->>>",topic+"_predicted")
            CacheHelper().set_json(topic+"_inference_frame", predicted_frame1)

            
            # predictor.input_frame  = frame2
            # predicted_frame1, detector_predictions,cord  = predictor.dummy()            
            # cv2.imshow('predicted_frame2',predicted_frame1)

            # predictor.input_frame  = frame3
            # predicted_frame1, detector_predictions,cord  = predictor.dummy()            
            # cv2.imshow('predicted_frame3',predicted_frame1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            t1 = datetime.now()
            print(f'Time taken for prediction of one frame {(t1-t0).total_seconds()} sec')

            
            torch.cuda.empty_cache()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
       # cap1.release()
        cv2.destroyAllWindows()



# def test_images(input_dir,out_dir):
#     with torch.no_grad():
#         predictor = Inference()

#         for img in glob.glob(input_dir+'*.jpg'):
#             frame1 = cv2.imread(img)
            
#             predictor.input_frame  = frame1
#             predicted_frame1, detector_predictions,cord  = predictor.dummy()
            
#             cv2.imwrite(out_dir+ img.split('\\')[-1],predicted_frame1)

            
#             torch.cuda.empty_cache()
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break


#est_images('C:\\Users\\lovel\\OneDrive\\Pictures\\Camera Roll\\New folder\\','C:\\Users\\lovel\\OneDrive\\Pictures\\Camera Roll\\New folder2\\')


def __main__():
# Create threads as follows
    thread_pool = {}  
    f = open('config.json', 'r')
    distros_dict = json.load(f)
    f.close()
    for distro in distros_dict:  
        if 'preprocess' not in distro:
            distro['preprocess'] = [] 
        thread_pool[distro['Camera_id']] = multiprocessing.Process(target=cam, args=(distro['Camera_id'],0))
        print()        
    for tt in thread_pool:
        thread_pool[tt].start()
    for tt in thread_pool:
        thread_pool[tt].join()
    
if __name__ == "__main__":
    __main__() 
    cv2.destroyAllWindows()
 