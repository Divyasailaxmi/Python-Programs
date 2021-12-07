from inference_module import *
from config_module import *



predictor = Inference()
conf = opt_config()
defects = conf.defects




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
        # self.redis_cache = redis.StrictRedis(host="164.52.194.78", port="8080", db=0, socket_timeout=1)
        self.redis_cache = redis.StrictRedis(host=settings.REDIS_CLIENT_HOST, port=settings.REDIS_CLIENT_PORT, db=0, socket_timeout=1)
        settings.REDIS_CLIENT_HOST
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



def get_defect_list(detector_predictions):
	# print(defects)
	defect_list = []
	for i in detector_predictions:
		if i in defects:
			defect_list.append(i)
	return defect_list


def check_kanban(defect_list):
	if bool(defect_list):
		is_accepted = "Rejected"
	else:
		is_accepted = "Accepted"
	return is_accepted


print(cv2.VideoCapture(0))

rch = CacheHelper()
def inference_frame():

	cap = cv2.VideoCapture(0)

	while True:
		ret,frame = cap.read()
		rch.set_json({"frame":frame})
		

		predictor.input_frame  = frame
		predicted_frame, detector_predictions,cord  = predictor.dummy()

		defect_list =  get_defect_list(detector_predictions)
		is_accepted = check_kanban(defect_list)

		print(is_accepted)

		
		rch.set_json({"predicted_frame":predicted_frame})
		rch.set_json({"is_accepted":is_accepted})
		rch.set_json({"defect_list":defect_list})

if __name__ == '__main__':
	inference_frame()

