from commonutils import *
import cv2
rch = CacheHelper()

while True:
    frame = rch.get_json("value0")
    # print(frame,"############")
    frame1 = rch.get_json("value2")
    # print(rch.get_json('str(i)'))
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',frame1)
    # cv2.imwrite('image.jpg',frame)


    cv2.waitKey(50)
    # cv2.destroyAllWindows()
    





    

