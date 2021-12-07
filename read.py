import cv2
path = r'C:\Users\Divya\Dropbox\My Dropbox Move\Desktop\out.jpg'
img = cv2.imread(path,0)
cv2.imshow('image',img)