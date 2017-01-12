# -*- coding: utf-8 -*-

import numpy as np
import cv2
import glob
import xml.etree.ElementTree as ET
import pdb

### 1-1. 'face_box'と'landmark'が書いてあるxmlファイルをインポートする
print("[1/3]face_boxの位置情報が入ったXMLファイルへのパスを入力してください。")
xml_path = raw_input()
# /Users/chihiro/Programs/dlib/DlibSample/Images/faces_12202016/training_with_face_landmarks_20161220.xml

#### 「異なるXMLファイルのパスならもう一度読み込む」みたいにしたかった。
# while True:
#     xml_path = raw_input()
#     try:
#         tree = ET.parse(xml_path)
#         root = tree.getroot()
#         break
#     except:
#         print("正しいパスを入力してください。")
#     break

if xml_path[-4:] != '.xml':
    print("hoge.xmlの形のパスを再入力してください")
    xml_path = raw_input

tree = ET.parse(xml_path)
root = tree.getroot()


print("[2/3: 顔写真の入ったディレクトリのパスを入力してください。]")
img_dir = raw_input()
# /Users/chihiro/Programs/dlib/DlibSample/Images/faces_12202016/Image
if img_dir[-1] != '/':
    img_dir += '/'

print("[3/3: 出力先のディレクトリへのパスを入力してください。]")
out_dir = raw_input()
# /Users/chihiro/Desktop/tmp_landed_images_20161225
if out_dir[-1] != '/':
    out_dir += '/'

for image in root.findall('.//image'):


    ## 画像を開く
    ### 画像のファイル名を取得
    img_name = image.attrib['file']
    print(img_name)
    if '/' in img_name:
        img_name = img_name.split('/')[-1]
    img = cv2.imread(img_dir + img_name)  # 画像を開く


    ## 顔枠をレンダーする
    ### 必要な値の準備
    box = image.find('box').attrib
    height = int(box['height'])
    left = int(box['left'])
    top = int(box['top'])
    width = int(box['width'])
    pt1 = (left, top)
    pt2 = (left + width, top + height)
    box_color = (0, 255, 0)
    ### 顔の枠をレンダリング
    img_box = cv2.rectangle(img, pt1, pt2, box_color)


    ## 輪郭点をレンダーする
    img_box_land = img_box
    text_color = (0, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for land in image.findall('.//part'):
        ### 必要な点の準備
        text = land.attrib['name']
        x = int(land.attrib['x'])
        y = int(land.attrib['y'])
        fontscale = 0.1
        # thickness = xxx
        # cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        img_box_land = img_box
        cv2.putText(img_box_land, text, (x, y), font, fontscale, text_color)
        ## 出力する
        if '.png' in img_name:
            out_name = img_name[:-4]
            out_name += '_' + text+ '_land.png'
        elif '.jpeg' in img_name:
            out_name = img_name[:-5]
            out_name += '_' + text+ '_land.jpeg'
        elif '.jpg' in img_name:
            out_name = img_name[:-4]
            out_name += '_' + text+ '_land.jpg'
        else:
            print("Warning: the pic file name: \"" + img_name + "\" might be wrong")
        cv2.imwrite(out_dir + out_name, img_box_land)


###########################################
### 参考 ##################################
###########################################
# image = root.findall('.//image')[0]
#
### ファイル名
# In [28]: image.attrib['file']
# Out[28]: 'Image/indoor_001.png'
#
### 顔の枠
# In [32]: image.find('box').attrib
# Out[32]: {'height': '288', 'left': '406', 'top': '18', 'width': '277'}
#
### 輪郭点
# In [40]: for land in image.findall('.//part'):
#     ...:     print(land.attrib)
#     ...:
# {'y': '91', 'x': '446', 'name': '0'}
# {'y': '119', 'x': '449', 'name': '1'}
# {'y': '151', 'x': '451', 'name': '2'}
#     ...:
# {'y': '241', 'x': '557', 'name': '66'}
# {'y': '240', 'x': '548', 'name': '67'}

# landmarks = {}
# for image in root.findall('.//image'):
#     tmp = image.attrib['file']
#     if tmp.index('/') > 0:
#         tmp = tmp.split('/')[-1]
#     image_file_names.append(tmp)
