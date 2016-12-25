image_names # 各 imageが入ってるやつ


# In [22]: ET.dump(img_xml)
# <image file="Image/indoor_001.png">
#     <box height="288" left="406" top="18" width="277" />
# </image>

# land_dir
# Out[24]: '/Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/07_landmarkdata_in_and_out/'


# img_xml  .... img_xml = land_file_name[i] 的なやつ
img_name = img_xml.attrib['file']
img_name = img_name.split("/")[1]
land_file_name = img_name.split(".")[0] + ".txt"
land_dir + land_name


lands = open(land_dir+land_name, 'r').read().split("\n")
lands = lands[:-1]

f = []
for land in lands:
    l = land.split(", ")
    f.append([l[0], l[1]])
lands = f

### こっからXMLに移植していく。

image = image_names[i]
land

for i, land in enumerate(lands):
    ET.SubElement(image, 'part', attrib = {'name': i, 'x' : land[0], 'y' : land[1]})



###############################################################
###############################################################
###############################################################
import numpy as np
import xml.etree.ElementTree as ET

### import xml
print("face_boxの位置情報が入ったXMLファイルへのパスを入力してください。")
xml_path = raw_input()

### XMLを読み込む
tree = ET.purse(xml_path)

### それぞれの顔のファイルを読み込むときのファイル名に変換する
lanfmark_txt_names = []
for elem in tree.find('images').findall('image'):
    lanfmark_txt_names.append(elem.attrib['file'])


