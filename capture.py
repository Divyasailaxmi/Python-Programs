import cv2

cam = cv2.VideoCapture(1)
cam.set(3,3840)
cam.set(4,2160)
cv2.namedWindow("test")

img_counter = 0
print(cam)
while True:

    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    frame1 = frame[413:1425,885:2885].copy()
    frame2 = cv2.resize(frame1,(640,480))
    cv2.imshow("test", frame2)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "C:\\Users\\Divya\\Desktop\\anomaly_images\\img{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame1)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()