# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET

print("Path the XML")
xml_path = raw_input()

if xml_path[-4:] != '.xml':
    rpint('hoge.xmlの形のパスを再入力してください')
    xml_path = raw_input()

tree = ET.parse(xml_path)
root = tree.getroot()

for image in root.findall('.//image'):
    file_name = image.attrib['file']
    if '/' in file_name:
        new_file_name = file_name.split('/')[-1]
        image.attrib['file'] = new_file_name

print("出力先のディレクトリへのパスを入力してください。")
out_dir = raw_input()
# /Users/chihiro/Desktop/tmp_landed_images_20161225
if out_dir[-1] != '/':
    out_dir += '/'


print("出力ファイル名を入力してください(例：abc.xml)")
out_name = raw_input()
# /Users/chihiro/Desktop/tmp_landed_images_20161225
if out_name[-4:] != '.xml':
    pint('hoge.xmlの形のパスを再入力してください')
    out_name = raw_input()

tree.write(out_dir + out_name)
