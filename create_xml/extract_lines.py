# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET

# ゴール：single_faceのディレクトリ下のみの学習データ(XMLファイル)を構築する

# import xml

# import file name

# extract lines by reffering filenames

# merge

print("Plese input a path to the original train data(xml format).")
xml_path = raw_input()

if xml_path[-1] != '/':
    xml_path += '/'

tree = ET.parse(xml_path)
root = tree.getroot()

