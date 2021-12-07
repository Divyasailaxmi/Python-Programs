import multiprocessing
import cv2
import queue
from multiprocessing import Queue

queue_from_cam = multiprocessing.Queue()

def cam_loop(queue_from_cam):
    print ('initializing cam')
    cam = cv.CaptureFromCAM(-1)
    print ('querying frame')
    img = cv.QueryFrame(cam)
    print ('queueing image')
    queue_from_cam.put(img)
    print ('cam_loop done')


cam_process = multiprocessing.Process(target=cam_loop,args=(queue_from_cam,))
cam_process.start()

while queue_from_cam.empty():
    pass

print ('getting image')
from_queue = queue_from_cam.get()
print ('saving image')
cv2.SaveImage('img.jpg',from_queue)
print ('image saved')
