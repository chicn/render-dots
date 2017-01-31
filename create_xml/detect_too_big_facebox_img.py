# -*- coding: utf-8 -*-

import numpy as np
import cv2
import xml.etree.ElementTree as ET

### import xml
xml_path = ""
while xml_path[-4:] != '.xml':
    print("[1/4]face_boxの位置情報が入ったXMLファイルへのパスを入力してください。")
    xml_path = raw_input()

tree = ET.parse(xml_path)
root = tree.getroot()


total_size, total_height, total_width = 0, 0, 0
average_size, average_height, average_width = 0, 0, 0
i = 0
for image in root.findall('.//image'):
    for box in image.findall('.//box'):
        img_name = image.attrib['file']
        height = int(box.attrib['height'])
        width = int(box.attrib['width'])

        print("Name: %s, Boxsize: %d x %d" % (img_name, height, width))

        # if height <= 80:
        #     if width <= 80:
        #         print(image.attrib['file'])

        total_size += height * width
        total_height += height
        total_width += width
        i += 1

total_size /= i + 1
total_height /= i + 1
total_width /= i + 1

print("average_size: %d, average_height: %d, average_width: %d" % (total_size, total_height, total_width))
