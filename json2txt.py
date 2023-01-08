import json
import os

json_path = './Annotations/'
txt_path = './labels/'

json_files = os.listdir(json_path)

box = []
point = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# point = [round(x, 8) for x in point]
box_point = ''

txt_file = ''

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

del_files('/home/sywen/Code/yolov7-pose/b529aar/labels/')


for json_file in json_files:
    with open('./Annotations/' + json_file,'r') as file:
        json_str = file.read()
        json_data = json.loads(json_str)

        # labels
        lables = json_data['shapes']

        # Norm
        for label in lables:
            # box xmin,ymin xmax, ymax  -> cx,cy width,height
            if label['label'] == 'drouge':
                cx = round((label['points'][0][0] + label['points'][1][0])/2/json_data['imageWidth'], 8)
                cy = round((label['points'][0][1] + label['points'][1][1])/2/json_data['imageHeight'], 8)
                width = round((label['points'][1][0] - label['points'][0][0])/json_data['imageWidth'], 8)
                height = round((label['points'][1][1] - label['points'][0][1])/json_data['imageHeight'], 8)

                label['points'][0][0] = cx
                label['points'][0][1] = cy
                label['points'][1][0] = width
                label['points'][1][1] = height
                box = label['points']
            # point
            for cnt in range(1,13):
                if label['label'] == str(cnt):
                    label['points'][0][0] = round(label['points'][0][0]/json_data['imageWidth'], 8)
                    label['points'][0][1] = round(label['points'][0][1]/json_data['imageHeight'], 8)
                    point[cnt-1] = label['points']

        # label
        box_point = '0 ' + str(box) + ' ' + str(point)
        box_point = box_point.replace('[', '').replace(']', '').replace(',', '')

        # Write
        txt_file = txt_path + json_file.split('.')[0] + '.txt'
        f = open(txt_file,'a', encoding='utf-8')
        f.write(box_point)
        f.close()
        print("Write " + txt_file + ": " + box_point)