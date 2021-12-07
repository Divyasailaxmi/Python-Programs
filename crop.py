import cv2
import glob
import os
import os.path

files = glob.glob("C:\\Users\\Divya\\Desktop\\original_images\\*.png")
out = "C:\\Users\\Divya\\Desktop\\out\\"
if not os.path.isdir(out):
    os.mkdir(out)
count = 0
for file in files:
    count += 1
    img = cv2.imread(file)
    crop_img = img[642:1463, 720:1090]    
    try:

        cv2.imwrite(out + "img" + str(count) + ".png", crop_img)
        if count >= 100:
                break
        print(count, "cropped successfull....", file)
    except:
        continue