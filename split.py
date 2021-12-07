
import os
import shutil
import time
from datetime import datetime


t1 = datetime.now()

path = 'D:\\3_PUNCH\\3_PUNCH\\'


def test_train_split(path):

	res = os.listdir(path)

	length = (len(res)/2 ) / 5

	if not os.path.isdir('test'):
		os.mkdir('test')
	if not os.path.isdir('train'):
		os.mkdir('train')

	# test = []
	# train = []

	count = 0
	for file in res:
		if file.endswith('.jpg'):
			count += 1
			if count <= length:
				# test.append(path+file)
				# test.append(path+file.split('.')[0]+'xml')
				print('copying into test..........',count)
				shutil.copyfile(path+file,'test/'+file)
				shutil.copyfile(path+file.split('.')[0]+'.xml','test/'+file.split('.')[0]+'.xml')

			else:
				# train.append(path+file)
				# train.append(path+file.split('.')[0]+'.xml')
				print('copying into train.......',count)
				shutil.copyfile(path+file,'train/'+file)
				shutil.copyfile(path+file.split('.')[0]+'.xml','train/'+file.split('.')[0]+'.xml')


	# print(len(test))
	# print(len(train))
	
	t2 = datetime.now()

	r = t2 - t1
	print('process finished in :' ,r)

test_train_split(path)





















