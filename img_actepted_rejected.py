# import cv2
# import imutils 
# original = cv2.imread("/home/divya/Downloads/indo_tpt/03_11_21_indo_view_all (41).jpg")
# new = cv2.imread("/home/divya/Downloads/indo_tpt/03_11_21_indo_view_all (20).jpg")
# #resize the images to make them small in size. A bigger size image may take a significant time
# #more computing power and time
# original = imutils.resize(original, height = 600)
# new = imutils.resize(new, height = 600)
# diff = original.copy()
# cv2.imshow("diff",diff)
# cv2.imwrite("diff.jpg",diff)
# cv2.absdiff(original, new,diff)
# gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
  
#  #increasing the size of differences after that we can capture them all
# for i in range(0,2):
#     dilated = cv2.dilate(gray.copy(), None, iterations= i+ 1)
#     (T, thresh) = cv2.threshold(dilated, 2, 255, cv2.THRESH_BINARY)
  
#  # now we have to find contours in the binarized image
#     cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     for c in cnts:
#      # nicely fiting a bounding box to the contour
#      (x, y, w, h) = cv2.boundingRect(c)
#      cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2)
#      cv2.imshow("new",new)
#  #remove comments from below 2 lines if you want to
#  #for viewing the image press any key to continue
#  #simply write the identified changes to the disk
#     cv2.imwrite("changes.jpg", new)   



import cv2
import glob
from datetime import datetime
import time
import streamlit as st

conf = opt_config()
defects = conf.defects
def get_defect_list(detector_predictions):
	# print(defects)
	defect_list = []
	for i in detector_predictions:
		if i in defects:
			defect_list.append(i)
	return defect_list


def check_kanban(defect_list):
	if bool(defect_list):
		is_accepted = "Rejected"
	else:
		is_accepted = "Accepted"
	return is_accepted

def inference_frame(frame):
	input_frame  = frame
	defect_list =  get_defect_list(detector_predictions)
	is_accepted = check_kanban(defect_list)

	return predicted_frame,detector_predictions,is_accepted




cap = cv2.VideoCapture('/home/divya/Desktop/Divya/4sec.mp4')
total_inspection = 0
total_accepted = 0
total_rejected = 0
btn = st.sidebar.radio('Radio Button',['b1','b2'])

df = pd.read_csv('reports.csv')
while True:
	ret, frame = cap.read()

