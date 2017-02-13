# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob
from scipy.io import loadmat

# Step 1 
# Lord .mat file containing Bounding Boxes
# And convert to be ready for making XML tree


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

# Step 2
# Create base of XML


# Step 3
# Prepare for lording annotation data