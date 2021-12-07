import cv2
import streamlit as st
import glob
import shutil
from datetime import datetime
import time
import pandas as pd
from worker_stream import *
import pyttsx3




rch = CacheHelper()

st.success('LIVE FEED')

run = st.checkbox('Run',value=True)
btn = st.sidebar.button('Push Button')


FRAME_WINDOW = st.image([])
FRAME_WINDOW_PRE = st.image([])

st.sidebar.markdown("<h1 style='text-align: center; color: green;'>Reports</h1>", unsafe_allow_html=True)


DEFECT_LIST = st.sidebar.info(None)
STATUS = st.sidebar.info(None)
REPORTS = st.sidebar.dataframe(None)

df = pd.read_csv('reports.csv')


def write_frames(name,frame):
	if not os.path.isdir('rejected_images'):
		os.makedirs('rejected_images')

	cv2.imwrite('rejected_images/'+name+str(datetime.now())+'.jpg',frame)


while run:
	frame = rch.get_json('frame')
	
	predicted_frame = rch.get_json('predicted_frame')
	detector_predictions = rch.get_json('defect_list')
	is_accepted = rch.get_json('is_accepted')
	
	if btn==True:

		predicted_frame1 = cv2.cvtColor(predicted_frame,cv2.COLOR_BGR2RGB)
		FRAME_WINDOW.image(predicted_frame1)
		df['total'][0] += 1
		if is_accepted == 'Accepted':		
			STATUS.success('Status: '+is_accepted)
			df['accepted'][0] += 1
			pyttsx3.say(is_accepted)

		if is_accepted == 'Rejected':
			STATUS.error('Status: '+is_accepted)
			df['rejected'][0] += 1
			write_frames(is_accepted,frame)
			write_frames(is_accepted,predicted_frame)
			pyttsx3.say(is_accepted)
			
		
		DEFECT_LIST.info('Defects: '+str(detector_predictions))
		time.sleep(1)
		btn = False
	
	else:
		predicted_frame = cv2.cvtColor(predicted_frame,cv2.COLOR_BGR2RGB)
		FRAME_WINDOW.image(predicted_frame)

		
	df.to_csv('reports.csv',header=True, index=False)
	REPORTS.dataframe(df)

else:
	st.header('Reports')
	st.dataframe(df)
