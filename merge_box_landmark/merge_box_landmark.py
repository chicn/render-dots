# -*- coding: utf-8 -*-

###########################################################
#
### How to use ###
# create a directory like "create_traindata"
# put those data as below in the same directory.
# 1. xml file with box data of face.
# 2. each file of images which contains landmark.
#
# Then, you'll find an output of xmldata as traindata.
#
###########################################################

import xml.etree.ElementTree as ET
import numpy as numpy


work_dir = "/Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/create_traindata/"
face_box_file = "output_20161209_100.xml"
tree = ET.parse(work_dir + face_box_file)  # 返値はElementTree型
elem = tree.getroot()  # ルート要素を取得(Element型)

print(elem.findtext(".//box"))