# -*- coding: utf-8 -*-

import numpy as np
import cv2
import glob
import math

############################
def read_xml():
    path = raw_input()
    if path[-4] != '.xml':
        path += '.xml'
    return path

def read_path():
    path = raw_input()
    if path[-1] != '/':
        path += '/'
    return path

def image_format():
    path = raw_input()
    if path != 'jpg':
        if path != 'jpeg':
            if path != 'png':
                print("couldn't recognize the format.")
    return path
############################
def get_img_info(path_to_img):
    img_matrix = cv2.imread(path_to_img, 1)

    height = img_matrix.shape[0]
    width  = img_matrix.shape[1]

    size = height * width
    ratio = size / 187500
    ratio = math.sqrt(ratio)
    if ratio < 1:
        ratio = 1

    return {'img': img_matrix, 'height': height, 'width': width, 'ratio': ratio}

def resize_image(path_to_img):

    # get info
    img_info = get_img_info(path_to_img)

    height_new = int(img_info['height'] / img_info['ratio'])
    width_new = int(img_info['width'] / img_info['ratio'])
    resized_img = cv2.resize(img_info['img'],(width_new, height_new))

    return resized_img
############################



print("[1]Please input a path to \"the directory of image data\".")
img_dir = read_path()

print("[2]Please input a \"TYPE\" of the image files. \n ex) png, jpeg, jpg")
img_format = image_format()

full_img_names = glob.glob(img_dir + "*." + img_format)

img_names = []
for i, img_name in enumerate(full_img_names):
    name = img_name[img_name.rfind('/')+1:]
    img_names.append(name)




print("[3]Pleasee input a path to \"the directory to save output images\".")
out_dir = read_path()

for img_name in full_img_names:
    resized_img = resize_image(img_name)

    name = img_name[img_name.rfind('/')+1:]
    name = name.split('.')
    out_name = name[0] + '_resized.' + name[1]

    cv2.imwrite(out_dir + out_name, resized_img)
