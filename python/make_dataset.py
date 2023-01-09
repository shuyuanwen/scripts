import os
import random
import shutil

path = '/home/sywen/Code/yolov7-pose/b529aar/'
ftrain = open(path + 'train.txt', 'w')
fval = open(path + 'val.txt', 'w')

trainval_percent = 0.7

images_path = '/home/sywen/Code/yolov7-pose/b529aar/lRGB/'
images_file = os.listdir(images_path)

total_jpg = [jpg for jpg in os.listdir(images_path) if jpg.split('.')[-1] == 'jpg']

num = len(total_jpg)
list = range(num)
tv = int(num * trainval_percent)
train = random.sample(list, tv)

# 删除文件下所有文件
def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)

del_files('/home/sywen/Code/yolov7-pose/b529aar/train/images/')
del_files('/home/sywen/Code/yolov7-pose/b529aar/train/labels/')
del_files('/home/sywen/Code/yolov7-pose/b529aar/test/images/')
del_files('/home/sywen/Code/yolov7-pose/b529aar/test/labels/')

for i in list:
    name = total_jpg[i] + '\n'
    if i in train:
        ftrain.write('/home/sywen/Code/yolov7-pose/b529aar/train/images/' + name)
        shutil.copyfile('/home/sywen/Code/yolov7-pose/b529aar/lRGB/' + total_jpg[i], '/home/sywen/Code/yolov7-pose/b529aar/train/images/' + total_jpg[i])
        shutil.copyfile('/home/sywen/Code/yolov7-pose/b529aar/labels/' + total_jpg[i].split('.')[0] + '.txt', '/home/sywen/Code/yolov7-pose/b529aar/train/labels/' + total_jpg[i].split('.')[0] + '.txt')
    else:
        fval.write('/home/sywen/Code/yolov7-pose/b529aar/test/images/' + name)
        shutil.copyfile('/home/sywen/Code/yolov7-pose/b529aar/lRGB/' + total_jpg[i], '/home/sywen/Code/yolov7-pose/b529aar/test/images/' + total_jpg[i])
        shutil.copyfile('/home/sywen/Code/yolov7-pose/b529aar/labels/' + total_jpg[i].split('.')[0] + '.txt', '/home/sywen/Code/yolov7-pose/b529aar/test/labels/' + total_jpg[i].split('.')[0] + '.txt')

