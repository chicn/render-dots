# -*- coding: utf-8 -*-

### Guideline
# このプログラムは、
# それぞれの画像に対する「整数の輪郭点データ」と、
# 永尾さんが作ってくれた「顔の位置データ」を、
# マージして使える学習データ(XML)を吐き出すためのプログラム
# 
# 1. txtデータの整形
# 2. XMLファイルの整形
# 3. txtをXMLファイルへマージ
# 4. 学習データを吐き出す

import numpy as np
# from xml.etree.ElementTree import *
import xml.etree.ElementTree as ET
import glob

#
# $ pwd
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W
#
# $ ls -1
# 01_Indoor_image
# 02_1_Indoor_landmark
# 02_2_indoor_landmark_round
# 03_Outdoor_image
# 04_1_Outdoor_landmark
# 04_2_outdoor_landmark_round
# 05_Indoor_dots
# 06_outdoor_dots
# create_traindata
#

### landの一番目の要素にどのイメージファイルのランドマークかを入れたい
#################################################################
#################################################################
#################################################################

### ここで、本当は(1)boxあり、(2)boxなしで分岐させたいが、
### 時間の都合上、既にboxのみのファイルを手で作り、それを使う。

print "(1/3)顔の位置ファイルのパスを入力してください"
face_box_path = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/create_traindata/box.xml

tree = ET.parse(face_box_path)  # 返値はElementTree型
root = tree.getroot()  # ルート要素を取得(Element型)

# 

image_file_name = [0] * len(root[2])
for i in range(len(root[2])):
    print(root[2][i].attrib['file'])
    image_file_name[i] = root[2][i].attrib['file']


image_num = len(image_file_name)
for i in range(image_num):
    image_file_name[i] = image_file_name[i].split("/")[1]

### "image_file_name" が今回欲しいファイル名


print "(2/3) 整数のランドマーク・ファイルが入ってるディレクトリへのパスを入力してください。"
land_dir = raw_input() + "/"
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/02_2_indoor_landmark_round

# land_filenames = glob.glob(land_dir + '*.txt')

land = [0] * image_num

for i in range(image_num):
    file_name = land_dir + image_file_name[i].split(".")[0] + ".txt"
    land[i] = open(file_name, "r").read().split("\n")


### land[i][-1] に '""' 入ってしまっている
for i in range(image_num):
    land[i] = land[i][0:-1]

# ### Ver.1 xmlファイルの形に変換
# # for i in range(image_num):
# #     for j in range(len(land[i])):
# #         x_y = land[i][j].split(", ")
# #         if j < 10:
# #             land[i][j] = "      <part name='0" + str(j) + "' x='" + x_y[0] + "' y='" + x_y[1] + "'/>"
# #         else:
# #             land[i][j] = "      <part name='" + str(j) + "' x='" + x_y[0] + "' y='" + x_y[1] + "'/>"


# ### Ver.2 parseで直接取り込むようのfor文
# xml_part = [""] * image_num
# for i in range(image_num):
#     for j in range(len(land[i])):
#         x_y = land[i][j].split(", ")
#         if j < 10:
#             # land[i][j] = "<part name='0" + str(j) + "' x='" + x_y[0] + "' y='" + x_y[1] + "'/>"
#             xml_part[i] += "<part name='0" + str(j) + "' x='" + x_y[0] + "' y='" + x_y[1] + "'/>"
#         else:
#             xml_part[i] += "<part name='" + str(j) + "' x='" + x_y[0] + "' y='" + x_y[1] + "'/>"

# ##### ET.fromstringができるようにXML構造をしっかりと持たせて、parseする
# for i in range(image_num):
#     xml_part[i] = "<parts>" + xml_part[i] + "</parts>"
#     xml_part[i] = ET.fromstring(xml_part[i])

# ##### boxの子要素として、書くpartを入れていく

# for box in root.findall('.//box'):
#     ET.SubElement(box, xml_part[i])

### Ver.3 要素は配列を保持し、attrib={} で扱いやすくしておく
xml_part = [[""] * len(land[i])] * image_num
for i in range(image_num):
    for j in range(len(land[i])):
        attrib = [""] * 3
        x_y = land[i][j].split(", ")
        if j < 10:
            attrib[0] = "0" + str(j)
        else:
            attrib[0] = str(j)
        attrib[1] = x_y[0]
        attrib[2] = x_y[1]
        xml_part[i][j] = attrib



##############################################
### 1と2で作った整形した文字列をあわせていく ###
##############################################

i = 0
for root_elem in root.iter('box'):
    if i > 0 :
        i += 1
    for j in range(len(land[i])):
        ET.SubElement(root_elem, 'part',
                                attrib = {'name': xml_part[i][j][0],
                                          'x' : xml_part[i][j][1],
                                          'y' : xml_part[i][j][2]
                                          }
                     )




print "(3/3) 保存したい学習データのパス+ファイル名を入力してください"
outdir = raw_input() + "/"
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/05_Indoor_circle
tree.write(outdir)