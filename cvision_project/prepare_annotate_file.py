import os, sys, random
import xml.etree.ElementTree as ET
import pandas as pd

data = pd.DataFrame()
ls_train = []
ls_test = []

classes = ["odo","0","1","2","3","4","5","6","7","8","9","km","."]
ratio = 0.9
dataset_dir = "C:/Users/chamandeep singh/Desktop/Cvision_own"

count = 0
# def gen_det_rec(classes, dataset_dir, ratio=1):
data = pd.DataFrame()
assert ratio <= 1 and ratio >= 0
img_dir = dataset_dir + "/" + "images_odometer/Odometer1"
label_dir = dataset_dir + "/" + "labels_odometer"
img_names = os.listdir(img_dir)
label_names = os.listdir(label_dir)
img_names.sort()
label_names.sort()
x = []
y = []
j = 0
for i in range(len(img_names)):
    if(img_names[i][:-4] in label_names[j]):
        x.append(img_names[i])
        y.append(label_names[j])
        j += 1
    i += 1
img_names = x
label_names = y
file_num = len(img_names)
assert file_num==len(label_names)

idx_random = list(range(file_num))
random.shuffle(idx_random)
idx_train=idx_random[:int(file_num*ratio)+1]
idx_val=idx_random[int(file_num*ratio)+1:]

for idx in range(file_num):
    if(label_names[idx].endswith('.xml')):
        each_img_path = img_dir + "/" + img_names[idx]
        each_label_path = label_dir+ "/" + label_names[idx]
        tree = ET.parse(each_label_path)
        root = tree.getroot()
        size = root.find('size')
        width = float(size.find('width').text)
        height = float(size.find('height').text)
        count += 1
        for obj in root.iter('object'):
            label = []
            cls_name = obj.find('name').text
            if cls_name not in classes:
                continue
            cls_id = classes.index(cls_name)
            xml_box = obj.find('bndbox')
            xmin = int(float(xml_box.find('xmin').text))
            ymin = int(float(xml_box.find('ymin').text))
            xmax = int(float(xml_box.find('xmax').text))
            ymax = int(float(xml_box.find('ymax').text))

            pat = each_img_path + ',' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)+ ',' +classes[cls_id]

            if idx in idx_train:
                ls_train.append(pat)
            else:
                ls_test.append(label)
data['format'] = ls_train
data.to_csv('annotate.txt', header=None, index=None, sep=' ')