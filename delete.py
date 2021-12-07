import cv2

vid = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(3)
cap3 = cv2.VideoCapture(4)
while True:
	ret, frame = vid.read()
	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()
	ret3, frame3 = cap3.read()
	#	cap1.set(cv2.CAP_PROP_AUTOFOCUS, 0)
	#	cap2.set(cv2.CAP_PROP_AUTOFOCUS, 0)̣	
	cv2.imshow('frame',frame)
	cv2.imshow('frame1',frame1)
	cv2.imshow('frame2',frame2)
	cv2.imshow('frame3',frame3)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()

