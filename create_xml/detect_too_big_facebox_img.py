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
