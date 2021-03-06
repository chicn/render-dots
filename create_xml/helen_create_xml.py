# -*- coding: utf-8 -*-

# HelenのデータセットからXMLファイルを構築してDlibに読み込ませられるXMLファイルを作成する

# 前準備
# 一つのディレクトリ下に以下のファイルを用意する
# 1. facebox のデータが入ったxmlファイル
# 2. annotationの点が入ったファイル(annotation ディレクトリ下に配置する)
#
# Helen_Dataset
# │─ helen_facebox.xml
# └─ annotation
#      └─ annotation_data1.txt
#      └─ annotation_data2.txt
#               │
#      └─ annotation_dataxx.txt

import numpy as np
import xml.etree.ElementTree as ET
import linecache
import glob

xml_path = ''
while xml_path[-4:] != '.xml':
    print("[1/3]face_boxの位置情報が入ったXMLファイルへのパスを入力してください。")
    xml_path = raw_input()
    if xml_path[-4:] != '.xml':
        print("hoge.xmlの形のパスを再入力してください")

print("[2/3] annotationファイルが入ったディレクトリへのパスを入力してください。")
annotation_dir = raw_input()

if annotation_dir[-1] != '/':
    annotation_dir += '/'

txt = ''
annotation_file_names = glob.glob(annotation_dir + '*.txt')

tree = ET.parse(xml_path)
root = tree.getroot()

for image in root.findall('.//image'):
    img_name = image.attrib['file']
    if '.' in img_name:
        img_original = img_name.split('.')[0]

    i = 0
    while img_original != txt:
        annotation_file_name = annotation_file_names[i]
        txt = linecache.getline(annotation_file_name, 1)[:-1]
        i += 1

    annotation = open(annotation_file_name).read().split('\r\n')
    if ',' not in annotation[0]:
        annotation.pop(0)
    for i, txt in enumerate(annotation):
        if txt == '':
            annotation.pop(i)
    for i, anno in enumerate(annotation):
        annotation[i] = anno.split(' , ')
        annotation[i][0] = str(int(round(float(annotation[i][0]))))
        annotation[i][1] = str(int(round(float(annotation[i][1]))))

    box = image.find('.//box')
    i = 0
    for anno in annotation:
        ET.SubElement(box, 'part',
                      attrib = {'name': str(i),
                                'x': anno[0],
                                'y': anno[1]
                               }
                      )
        i += 1

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

out_path = ''
while out_path[-4:] != '.xml':
    print("[3/3]保存したい学習データのパス+ファイル名を入力してください")
    out_path = raw_input()
    if out_path[-4:] != '.xml':
        print("/aa/bb/hoge.xmlの形のパスを再入力してください")
tree.write(out_path, encoding='utf-8')
