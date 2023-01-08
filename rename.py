import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
import os
from PIL import Image
import shutil

old_path = '/home/sywen/temp/2023/'
new_path = "/home/sywen/temp/GRAY/GRAY"


if __name__ == '__main__':
    grays = os.listdir(old_path)
    # gray_list = [x.split(".")[0].split("_")[1] for x in gray].sort()
    grays.sort(key=lambda x:int((x[:-4])[11:])) #将'.jpg'左边的字符转换成整数型进行排序

    frame_count = 0
    cnt = 0
    for gray in grays:
        if frame_count % 10 == 0:
            shutil.copyfile(old_path + gray, new_path + str(cnt).zfill(4) + ".bmp")
            print("Write" + new_path + str(cnt).zfill(4) + ".bmp")
            cnt += 1
        frame_count += 1 
