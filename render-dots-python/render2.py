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

image_file_name = [0] * len(root[2])

