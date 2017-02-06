# -*- coding: utf-8 -*-

import numpy as np
import glob
import xml.etree.ElementTree as ET


# XMLファイルを読み込む
# 10毎に要素数を増やす

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


xml_path = []
print("全てのiBugの情報が入ったxmlファイルへのパスを入力してください。")
# /Users/chihiro/dlib-19.1/images/ibug_simulation/training_with_face_landmarks.xml
while xml_path[-4:] != '.xml':
    xml_path = raw_input()

iterater = []
for i in range(60, 601):
    if i%10 == 0:
        iterater.append(i)

# tree.write('output.xml')

print("出力先のディレクトリへのパスを入力してください")
out_dir = raw_input()
# /Users/chihiro/dlib-19.1/images/ibug_simulation/
if out_dir[-1] != '/':
    out_dir += '/'

for i in iterater:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for img in root.findall('.//image'):
        name = img.attrib['file'][6:-4]
        icr = name.split('_') # ['indoor', '050']
        if icr[0] == 'indoor':
            num = int(icr[1])
        # if icr[0] == 'outdoor':
        #     num = int(icr[1]) + 300
        else:
            num = int(icr[1]) + 300
        if num > i:
            root[2].remove(img)

    tree.write('%straining_with_face_landmarks_%d.xml' % (out_dir, i))

