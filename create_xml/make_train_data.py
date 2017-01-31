# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET

### import xml
print("[1/4]face_boxの位置情報が入ったXMLファイルへのパスを入力してください。")
xml_path = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/output_20161216_all.xml

if xml_path[-4:] != '.xml':
    xml_path += '.xml'

### XMLを読み込む
tree = ET.parse(xml_path)
root = tree.getroot()

### それぞれの顔のファイルを読み込むときのファイル名に変換する
landmark_txt_names = []
for elem in tree.find('images').findall('image'):
    landmark_txt_names.append(elem.attrib['file'])

for i, f_name in enumerate(landmark_txt_names):
    tmp = f_name.split('/')[1]
    tmp = tmp.split('.')[0]
    landmark_txt_names[i] = tmp + ".txt"

# landmark_txt_namesの完成
# In [31]: landmark_txt_names
# Out[31]:
# ['indoor_001.txt',
#  'indoor_002.txt',
#  ...
#   'outdoor_299.txt',
#  'outdoor_300.txt']

print("[2/4] landmark_locationのファイル達が入ったディレクトリのパスを入力してください。")
land_dir = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/07_landmarkdata_in_and_out/
if land_dir[-1] != '/':
    land_dir = land_dir + '/'


### xml に入れやすいようにインポートする。
### 「landmark_locations」に各ファイルのランドマークが入る。
landmark_locations = []
for landmark_txt_name in landmark_txt_names:
    pts = open(land_dir + landmark_txt_name)
    pts = pts.read().split("\n")

    
    pts = pts[:68]

    tmp = []
    for i, pt in enumerate(pts):
        tmp = pt.split(', ')
        pts[i] = [tmp[0], tmp[1]]

    landmark_locations.append(pts)



### xmlにSubElement していく

for index, box in enumerate(root.findall('.//box')):
    for index, landmark_location in enumerate(landmark_locations[index]):
        ET.SubElement(box, 'part', attrib = {
                                             'name': str(index),
                                             'x': landmark_location[0],
                                             'y': landmark_location[1]
                                            }
                     )

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

print("[3/4] 完成した訓練データ(.xml)を保存したいディレクトリのパスを入力してください。")
out_dir = raw_input()

if out_dir[-1] != '/':
    out_dir += '/'

print("[4/4] 完成した訓練データのファイル名を入力してください。")
out_file_name = raw_input()

if out_file_name[-4:] != '.xml':
    out_file_name += '.xml'

tree.write(out_dir + out_file_name)
