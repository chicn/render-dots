# -*- coding: utf-8 -*-

import numpy as np
import cv2
import glob

print("[1]Please input a path to \"the directory of image data\".")
img_dir = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/07_Single_Face_selected

if img_dir[-1] != '/':
    img_dir += '/'

print("[2]Please input a \"TYPE\" of the image files. \n ex) png, jpeg, jpg")
img_format = raw_input()
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W_single_multi/05_Single_Face

if img_format != 'jpg':
    if img_format != 'jpeg':
        if img_format != 'png':
            print("couldn't recognize the format.")

img_dir += '*.' + img_format

full_img_names = glob.glob(img_dir)

img_names = []
for i, img_name in enumerate(full_img_names):
    name = img_name[img_name.rfind('/')+1:]
    img_names.append(name)


def resize_image(img_file_name):
    # read image
    img = cv2.imread(img_file_name, 1)

    # get the size
    height = img.shape[0]
    width = img.shape[1]

    # check the size
    size = height * width

    ratio = size / 187500

    if ratio != 0:
        height_new = height / ratio
        width_new = width / ratio
        resized_img = cv2.resize(img,(width_new, height_new))
    else:
        resized_img = img

    return(resized_img)

print("[3]Pleasee input a path to \"the directory to save output images\".")
out_dir = raw_input()
if out_dir[-1] != '/':
    out_dir += '/'

for img_name in full_img_names:
    resized_img = resize_image(img_name)

    name = img_name[img_name.rfind('/')+1:]
    name = name.split('.')
    name = name[0] + '_half.' + name[1]

    cv2.imwrite(out_dir + name, resized_img)

