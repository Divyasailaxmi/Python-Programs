import os
import xml.etree.ElementTree as ET

path = '/home/divya/Downloads/indo_tpt/'

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
					# print(file)
					
	# print(len(class_names))
	# print(class_names.count('RedSpring'))
	# class_names = set(class_names)
	# class_names = list(class_names)
	# class_names.sort()

	temp = {}
	for i in class_names:
		temp[i] = class_names.count(i)

	# print(class_names)
	print(temp)

all_class_names(path)

# ['RedSpring', 'Screws', 'Spring_Absence', 'Spring_Presence']
# ['RedSpring', 'Screws', 'Spring_Absence', 'Spring_Presence']


# RedSpring = 643 + 159
# Screws = 1947 + 484
# Spring_Absence = 457 + 118
# Spring_Presence = 2112 + 519