# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob

# ゴール：single_faceのディレクトリ下のみの学習データ(XMLファイル)を構築する

# import xml

# import file name

# extract lines by reffering filenames

# out

#######################################
print("[1]Plese input a path to \"the original train data(xml format)\".")
xml_path = raw_input()
# /Users/chihiro/Programs/dlib/DlibSample/Images/faces_12202016/training_with_face_landmarks.xml

if xml_path[-4:] != '.xml':
    xml_path += '.xml'

tree = ET.parse(xml_path)
root = tree.getroot()



#######################################
print("[2]Please input a path to \"the directory of image data\".")
img_dir = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face

if img_dir[-1] != '/':
    img_dir += '/'

print("[3]Please input a \"TYPE\" of the image files. \n ex) png, jpeg, jpg")
img_format = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face

if img_format != 'jpg':
    if img_format != 'jpeg':
        if img_format != 'png':
            print("couldn't recognize the format.")

img_dir += '*.' + img_format

img_names = glob.glob(img_dir)
original_img_names = img_names

### 特別使用
for i, img_name in enumerate(img_names):
    slash_index = img_name.rfind('/')
    img_names[i] = img_name[slash_index+1:]
    img_names[i] = 'Image/' + img_names[i]




#######################################
for image in root.findall('.//image'):
    if image.attrib['file'] not in img_names:
        root[2].remove(image)

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(root)

print("[4] 完成した訓練データ(.xml)を保存したいディレクトリのパスを入力してください。")
out_dir = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face
if out_dir[-1] != '/':
    out_dir += '/'

print("[5] 完成した訓練データのファイル名を入力してください。")
out_file_name = raw_input()

if out_file_name[-4:] != '.xml':
    out_file_name += '.xml'

tree.write(out_dir + out_file_name)