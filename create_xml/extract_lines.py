# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob

# ゴール：single_faceのディレクトリ下のみの学習データ(XMLファイル)を構築する

# import xml

# import file name

# extract lines by reffering filenames

# merge

#######################################
print("Plese input a path to \"the original train data(xml format)\".")
xml_path = raw_input()

if xml_path[-4:] != '.xml':
    xml_path += '.xml'

tree = ET.parse(xml_path)
root = tree.getroot()



#######################################
print("Please input a path to \"the directory of image data\".")
img_dir = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face

if img_dir[-1] != '/':
    img_dir += '/'

print("Please input a \"TYPE\" of the image files. \n ex) png, jpeg, jpg")
img_format = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face

if img_format != 'jpg':
    if img_format != 'jpeg':
        if img_format != 'png':
            print("couldn't recognize the format.")

img_dir += '*.' + img_format

img_names = glob.glob(img_dir)



#######################################
