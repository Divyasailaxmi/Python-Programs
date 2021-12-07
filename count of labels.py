import os
import xml.etree.ElementTree as ET
path = '/home/lincode/yolov5/Data_punch/Data_Punch/images/train/'
def all_class_names(path):
	class_names = []
	files = os.listdir(path)
	for file in files:
		if file.endswith('.xml'):
			tree = ET.parse(path+file)
			root = tree.getroot()
			for elt in root.iter():
				if elt.tag == 'name':
					class_names.append(elt.text)

	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)
	print(temp)

all_class_names(path)