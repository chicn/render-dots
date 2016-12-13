# -*- coding: utf-8 -*-

import numpy as np
import cv2
import pdb

print "(1/5)Please type the directory of images for input."
indir = raw_input() + "/"
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/01_Indoor
print "(2/5)Please type the directory of images for output."
outdir = raw_input() + "/"
# /Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/05_Indoor_circle

print "(3/5)Please type the file name which contains the list of image file names."
filename = raw_input()
filename = open(indir + "/" + filename).read().split("\n")

print "(4/5)Please type the directory of landmarks for input."
landmark_dir = raw_input() + "/"

print "(5/5)Please type the file name which contains the list of landmark file names."
landmark_file_name = raw_input()
# landmark_file_name = open(landmark_dir + "/" + landmark_file_name).read().split("\n")
landmark_file_name = open(landmark_dir + landmark_file_name).read().split("\n")


def put_text(img, x, y, landmark):
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(landmark)):
        # put text.
        # cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        cv2.putText(img, str(i+1), (x, y), font, 0.3, (3,198,2), 2, cv2.LINE_AA)


if (len(filename) != len(landmark_file_name)):
    "画像とランドマークのファイル数が一致しません。"
else:
    for i in range(len(filename)):
        # Landmark File の 読み込み
        landmark = open(landmark_dir + landmark_file_name[i])
        landmark = landmark.read().split("\n")[:-1]
        for j in range(len(landmark)):
            # pdb.run('mymodule.test()')
            tmp = [0] * 2
            # tmp[0] = int(landmark[j].split(", ")[0])
            # tmp[1] = int(landmark[j].split(", ")[1])
            tmp[0] = int(landmark[j].split(", ")[0])
            tmp[1] = int(landmark[j].split(", ")[1])
            landmark[j] = tmp

        # render 対象の写真
        img = cv2.imread(indir + filename[i])
        # renderの元になるlocationが入ったデータ => landmark
        for k in range(len(landmark)):
            put_text(img, landmark[k][0], landmark[k][1], landmark)
        # render 終了
        cv2.imwrite(outdir + filename[i], img)
