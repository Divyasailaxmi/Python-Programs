import cv2
import numpy

large_image  = cv2.imread("C:\\Users\\Divya\\Desktop\\img.jpg")
small_image = cv2.imread("C:\\Users\\Divya\\Desktop\\template1.jpg")

null, w, h = small_image.shape[::-1]

res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
loc = numpy.where(res >= 0.7)

for pt in zip(*loc[::-1]):
    suh = cv2.rectangle(small_image, pt, (pt[0] + w, pt[1] + h), (0, 66, 255), 1)

cv2.imwrite('output.jpg', suh)



# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Divya\\Desktop\\img.jpg")
# grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# template = cv2.imread("C:\\Users\\Divya\\Desktop\\template1.jpg",0)
# w,h = template.shape[::-1]
# res = cv2.matchTemplate(grey,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where(res >= threshold)
# for i in zip(*loc[::-1]):
#   cv2.rectangle(img,i,(i[0] + w , i[1] + h),(0,0,255),2)
# cv2.imshow("img.jpg",loc)
# cv2.waitKey(0)
# cv2.destroyAllWindows()