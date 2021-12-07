import cv2

vid = cv2.VideoCapture(2)
# cap1 = cv2.VideoCapture("C:\\Users\\Divya\\Desktop\\burr.mp4")
# cap2 = cv2.VideoCapture("C:\\Users\\Divya\\Desktop\\ChamferAP.mp4")
# cap3 = cv2.VideoCapture("C:\\Users\\Divya\\Desktop\\ThreadAP_holes_dent.mp4") 


all_vid = [vid]

for i in all_vid:
	frame_width = int(vid.get(3))
	frame_height = int(vid.get(4))
# size = (frame_width,frame_height) 
	res = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


while True:
	ret, frame = vid.read()
	# ret1, frame1 = cap1.read()
	# ret2, frame2 = cap2.read()
	# ret3, frame3 = cap3.read()
	# ret4, frame2 = cap4.read()
	cv2.imshow('frame',frame)
	res.write(frame)
	# cv2.imshow('frame1',frame1)
	# res1.write(frame1)
	# cv2.imshow('frame2',frame2)
	# res2.write(frame2)
	# cv2.imshow('frame3',frame3)
	# res3.write(frame3)
	# cv2.imshow('frame4',frame4)

	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

vid.release()
res.release()
# res1.release()
# res2.release()
# res3.release()
# cap1.release()
# cap2.release()
# cap3.release()
# cap4.release()
cv2.destroyAllWindows()

