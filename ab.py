import cv2
import numpy as np
  
# read the images
p2_cam1 = cv2.imread('p2_cam1.jpg')
p2_cam1 = cv2.resize(p2_cam1 ,(1920,1080))

p2_cam2 = cv2.imread('p2_cam2.jpg')
p2_cam2 = cv2.resize(p2_cam2,(1920,1080))

p2_cam3 = cv2.imread('p2_cam3.jpg')
p2_cam3 = cv2.resize(p2_cam3,(1920,1080))

p2_cam4 = cv2.imread('p2_cam4.jpg')
p2_cam4 = cv2.resize(p2_cam4,(1920,1080))

p2_cam5 = cv2.imread('p2_cam5.jpg')
p2_cam5 = cv2.resize(p2_cam5,(1920,1080))

p2_cam6 = cv2.imread('p2_cam6.jpg')
p2_cam6 = cv2.resize(p2_cam6,(1920,1080))

p2_cam7 = cv2.imread('p2_cam7.jpg')
p2_cam7 = cv2.resize(p2_cam7,(1920,1080))

p2_cam8 = cv2.imread('p2_cam8.jpg')
p2_cam8 = cv2.resize(p2_cam8,(1920,1080))

p2_cam9 = cv2.imread('p2_cam9.jpg')
p2_cam9 = cv2.resize(p2_cam9,(1920,1080))

p2_cam10 = cv2.imread('p2_cam10.jpg')
p2_cam10 = cv2.resize(p2_cam10,(1920,1080))

cam1 = cv2.imread('cam1.jpg')
cam1 = cv2.resize(cam1 ,(1920,1080))

cam2 = cv2.imread('cam2.jpg')
cam2 = cv2.resize(cam2,(1920,1080))

cam3 = cv2.imread('cam3.jpg')
cam3 = cv2.resize(cam3,(1920,1080))

cam4 = cv2.imread('cam4.jpg')
cam4 = cv2.resize(cam4,(1920,1080))

cam5 = cv2.imread('cam5.jpg')
cam5 = cv2.resize(cam5,(1920,1080))

cam6 = cv2.imread('cam6.jpg')
cam6 = cv2.resize(cam6,(1920,1080))

cam7 = cv2.imread('cam7.jpg')
cam7 = cv2.resize(cam7,(1920,1080))

cam8 = cv2.imread('cam8.jpg')
cam8 = cv2.resize(cam8,(1920,1080))

cam9 = cv2.imread('cam9.jpg')
cam9 = cv2.resize(cam9,(1920,1080))

cam10 = cv2.imread('cam10.jpg')
cam10 = cv2.resize(cam10,(1920,1080))


con = np.concatenate((p2_cam1,cam1),  axis=1)
con1 = np.concatenate((p2_cam2,cam2), axis=1)
con2 = np.concatenate((p2_cam3,cam3), axis=1)
con3 = np.concatenate((p2_cam4,cam4), axis=1)
con4 = np.concatenate((p2_cam5,cam5), axis=1)
con5 = np.concatenate((p2_cam6,cam6), axis=1)
con6 = np.concatenate((p2_cam7,cam7), axis=1)
con7 = np.concatenate((p2_cam8,cam8), axis=1)
con8 = np.concatenate((p2_cam9,cam9), axis=1)
con9 = np.concatenate((p2_cam10,cam10), axis=1)
# con = cv2.hconcat([img1, img2])
# con2 = cv2.hconcat([img3, img4])

both = np.concatenate((con,con1,con2,con3,con4,con5,con6,con7,con8,con9),axis=0)
cv2.imwrite("D:/both.jpg",both)

cv2.imshow("img",both)
cv2.waitKey(2)
cv2.destroyAllWindows()
