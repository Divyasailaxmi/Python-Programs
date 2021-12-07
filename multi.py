import cv2

vid = cv2.VideoCapture("C:\\Users\\Divya\\Desktop\\burr.mp4")
vid1 = cv2.VideoCapture("C:\\Users\\Divya\\Desktop\\ChamferAP.mp4")


if (vid.isOpened() == False): 
    print("Error reading video file")
frame_width = int(vid.get(3))
frame_height = int(vid.get(4)) 
res = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

if (vid1.isOpened() == False): 
    print("Error reading video file1")
frame_width = int(vid1.get(3))
frame_height = int(vid1.get(4)) 
res1 = cv2.VideoWriter('test1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


while True:
	ret, frame = vid.read()
	ret1,frame1 = vid1.read()
	cv2.imshow('frame',frame)
	res.write(frame)
	cv2.imshow('frame1',frame1)
	res1.write(frame1)
	


	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

vid.release()
res.release()
vid1.release()
res1.release()
cv2.destroyAllWindows()

