# -*- coding: utf-8 -*-

import numpy as np
import xml.etree.ElementTree as ET
import glob
from scipy.io import loadmat

# Step 1 
# Lord .mat file containing Bounding Boxes
# And convert to be ready for making XML tree


def lord_bounding_box_mat(path):
    mat_path = ''
    while mat_path[-4:] != '.mat':
        print("face_boxの情報が入った\".mat\"ファイルへのパスを入力してください。")
        mat_path = raw_input()

        mat_dict = {}
        mat_dict.update(loadmat(mat_path))

        box = mat_dict['bounding_boxes']

        box_dict = {}

        for i in range(len(box[0])):
            box_dict.update{box[0][i][0][0][0][0]:
                            {
                                'pt1' : box[0][i][0][0][1][0][0]
                                'pt2' : box[0][i][0][0][1][0][1]
                                'pt3' : box[0][i][0][0][1][0][2]
                                'pt4' : box[0][i][0][0][1][0][3]
                            }
                           }






# Step 2
# Create base of XML


# Step 3
# Prepare for lording annotation data