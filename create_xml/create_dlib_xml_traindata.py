# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob
from scipy.io import loadmat


def load_bounding_box_mat():
    mat_path = ''
    while mat_path[-4:] != '.mat':
        print("face_boxの情報が入った\".mat\"ファイルへのパスを入力してください。")
        mat_path = raw_input()

        mat_dict = {}
        mat_dict.update(loadmat(mat_path))
        np_box = mat_dict['bounding_boxes'][0]
        box_info = []

        # organizing box_info array
        for i in np_box:
            box_info.append([i[0][0][0][0], i[0][0][2].tolist()[0]])

        # turn numbers into integer
        for i in range(len(box_info)):
            for j in range(4):
                box_info[i][1][j] = int(round(box_info[i][1][j]))

    return box_info
     # [u'296814969_3.jpg', [266, 293, 566, 563]]


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def dlibRoot():
    root = ET.fromstring('<dataset><name>Training faces</name><comment/><images/></dataset>')
    return root


def load_annotations(file_name):
    annotations = open(file_name).read().split("\n")[3:-1]
    return annotations


def roundAnnotations(annotations):
    out_array = []
    for i, anno in enumerate(annotations):
        tmp = anno.split(' ')
        out_array.append([int(round(float(tmp[0]))), int(round(float(tmp[1])))])
    return out_array


# a = makeTreeBranch(root, info[1:4], rounded_pts)
def makeTreeBranch(root_element, box_info, annotations):
    imageBranch = ET.SubElement(root_element, 'image', attrib={'file': box_info[0]})
    boxBranch = ET.SubElement(imageBranch, 'box', attrib={'top': str(box_info[1][1]),
                                                          'left': str(box_info[1][0]),
                                                          'width': str(box_info[1][3] - box_info[1][1]),
                                                          'height': str(box_info[1][2] - box_info[1][0])})
    for i, anno in enumerate(annotations):
        if i < 10:
            partBranch = ET.SubElement(boxBranch, 'part', attrib={'name': '0'+str(i),
                                                                  'x': str(anno[0]),
                                                                  'y': str(anno[1])})
        else:
            partBranch = ET.SubElement(boxBranch, 'part', attrib={'name': str(i),
                                                                  'x': str(anno[0]),
                                                                  'y': str(anno[1])})
    return root_element


############# main ###################
# 顔枠の情報を取得
box_info = load_bounding_box_mat()
# XMLのベースを用意
elem = dlibRoot()
images = elem.find('.//images')


# 輪郭点ファイル取得の用意
print("輪郭点ファイルが入ったディレクトリへのパスを入力してください。")
anno_dir = raw_input()
if anno_dir[-1] != '/':
    anno_dir += '/'
# /Users/chihiro/Documents/08.Jolie-Joli/Images/helen_data/annotation_68pts/test/

 
for info in box_info:
    img_name = info[0]
    name = img_name.split('.')[0]
    pts_name = name + '.pts'

    pts = load_annotations(anno_dir + pts_name)
    rounded_pts = roundAnnotations(pts)

    makeTreeBranch(images, info, rounded_pts)


indent(elem)
tree = ET.ElementTree(elem)
print("出力したいディレクトリへのパスを入力してください")
out_dir = raw_input()
if out_dir[-1] != '/':
    out_dir += '/'
out_name = ''
while out_name[-4:] != '.xml':
    print("出力したいファイル名を入力してください")
    out_name = raw_input()
tree.write(out_dir + out_name, encoding="ISO 8859-1")
