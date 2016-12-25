# -*- coding: utf-8 -*-

import numpy as np
import cv2
import glob
import xml.etree.ElementTree as ET
import pdb

## 手順
### 1-1. 'face_box'と'landmark'が書いてあるxmlファイルをインポートする
### 1-2. XMLファイルをレンダリングに使えるように分解しておく
### 2. レンダリング
### 2-1. 写真をインポート
### 2-2. 対応するXMLを元に写真に'face_box'と'landmark'をレンダリングする
### 3. 出力



### 1-1. 'face_box'と'landmark'が書いてあるxmlファイルをインポートする

print("[1/3] face_boxとlandmarkを示すファイルのパスを入力してください\n\
ex) /Users/chihiro/Programs/dlib/DlibSample/Images/faces_12202016/training_with_face_landmarks_20161220.xml")

#### 「異なるXMLファイルのパスならもう一度読み込む」みたいにしたかった。
# while True:
#     land_path = raw_input()
#     try:
#         tree = ET.parse(land_path)
#         root = tree.getroot()
#         break
#     except:
#         print("正しいパスを入力してください。")
#     break

land_path = raw_input()
tree = ET.parse(land_path)
root = tree.getroot()
# images_xml = root.find('images') # 'images' 以下のみのXMLにする



### 1-2. XMLファイルをレンダリングに使えるように分解しておく
image_file_names = []

for image in root.findall('.//image'):
    tmp = image.attrib['file']
    if tmp.index('/') > 0:
        tmp = tmp.split('/')[-1]
    image_file_names.append(tmp)



### 2. レンダリング
### 2-1. 写真をインポート
def put_text(img, x, y, landmark, color=(3, 198, 2):
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(landmark)):
        # put text.
        cv2.putText(img, str(i+1), (x, y), font, 0.3, (3,198,2), 2, cv2.LINE_AA)

print("[2/3] 画像が入ったディレクトリのパスを入力してください。")
img_dir = raw_input() + "/"

# /Users/chihiro/Programs/dlib/DlibSample/Images/faces_12202016/Image

if img_dir[-1] != '/':
    img_dir += '/'






# i番目の写真にrender
landmark = root[2][i]

# name = j の x の値
root[2][i][0][j].attrib['x']



img = cv2.imread(img_dir + image_file_name[i])



# cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) → None
color_box = (255, 0, 0)
# In [59]: landmark[0].attrib
# Out[59]: {'height': '288', 'left': '406', 'top': '18', 'width': '277'}
cv2.rectangle(img, (18, 406), (18+288, 406+277), color_box)

cv2.imwrite('/Users/chihiro/Desktop/sample_box.png',img)







#################### テスト


image_all = images_xml.findall('image')

for image in image_all:
    if len(image.findall('box')) > 1:
        break
    else:
        box = image.find('box').attrib
        height = int(box['height'])
        left = int(box['left'])
        top = int(box['top'])
        width = int(box['width'])

        pt1 = (left, top)
        pt2 = (left + width, top + height)

        image_name = image.attrib['file']
        img = cv2.imread(img_dir + image_name)

        box_color = (0, 255, 0)

        img_box = cv2.rectangle(img, pt1, pt2, box_color)

        # parts = image.find('box').findall('part')

        parts = []
        for part in image.find('box').findall('part'):
            parts.append(part.attrib)


        font = cv2.FONT_HERSHEY_SIMPLEX
        for part in parts:
            # cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
            text = int(part['name']) + 1
            org = (int(part['x']), int(part['y']))
            fontscale = min(img.shape[:-1]) / 5000
            if fontscale == 0:
                fontscale = 1
            text_color = (3, 198, 2)
            thickness = min(img.shape[:-1]) / 1000
            if thickness == 0:
                thickness = 1

            cv2.putText(img_box, str(text), org, font, fontscale, text_color[thickness])




# imageのサイズ
# img.shape
# 
# 適切なポイント数を測るために小さい方を採用する
# min(img.shape[:-1])


# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



print("[3/3] 画像を入れるディレクトリのパスを入力してください。")
out_dir = raw_input() + "/"
