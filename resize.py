import glob
import cv2

path = 'C:\\Users\\Divya\\Pictures\\Camera Roll\\'

res = glob.glob(path+'*.jpg')

for file in res:
	print(file)
	img = cv2.imread(file)
	img = cv2.resize(img,(1920,1080))
	cv2.imwrite(path+file.split('\\')[-1],img)

