# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob
import cv2
import math

############################
def read_xml():
    path = raw_input()
    if path[-4] != '.xml':
        print('Please type a path like \'hoge/hogehoge.xml\'')
    return path

def read_path():
    path = raw_input()
    if path[-1] != '/':
        path += '/'
    return path
############################

# XMLを読む

print("[1/3]face_boxの位置情報が入ったXMLファイルへのパスを入力してください")
xml_path = read_xml()

tree = ET.parse(xml_path)
root = tree.getroot()

print("[2/3]XMLに対応した画像が入ったディレクトリへのパスを入力してください")
img_dir = read_path()

for image in root.findall('.//image'):
    # 取得する画像名を取得
    img_name = image.attrib['file']

    # 画像のインポート
    img_matrix = cv2.imread(img_dir + img_name)

    # 画像のratioを取得
    ## img
    img_height = img_matrix.shape[0]
    img_width  = img_matrix.shape[1]
    img_size = img_height * img_width
    ratio = img_size / 187500
    ratio = math.sqrt(ratio)
    if ratio < 1:
        ratio = 1


    if ratio != 1:
        ## box
        box = image.find('.//box')
        box.attrib['height'] = str(int(int(box.attrib['height']) / ratio))
        box.attrib['width'] = str(int(int(box.attrib['width']) / ratio))
        box.attrib['left'] = str(int(int(box.attrib['left']) / ratio))
        box.attrib['top'] = str(int(int(box.attrib['top']) / ratio))

        ## part
        for part in image.findall('.//part'):
            part.attrib['x'] = str(int(int(part.attrib['x']) / ratio))
            part.attrib['y'] = str(int(int(part.attrib['y']) / ratio))
    # 出力
print("[3/3] 新しく出力したいXMLファイルのフルパスを入力して下さい")
out_xml_path = raw_input()
if out_xml_path[-4:] != '.xml':
    print("hoge.xmlの形のパスを再入力してください")
    out_xml_path = raw_input()

tree.write(out_xml_path)
