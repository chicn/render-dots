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
        landmark = landmark.read().split("\n")
        for k in range(len(landmark)):
            tmp = [0] * 2
            tmp[0] = int(landmark[k].split(", ")[0])
            tmp[1] = int(landmark[k].split(", ")[1])
            landmark[k] = tmp

        # render 対象の写真
        img = cv2.imread(indir + filename[i])
        # renderの元になるlocationが入ったデータ => landmark
        for j in range(len(landmark)):
            put_text(img, landmark[i][0], landmark[i][1], landmark)
        # render 終了
        cv2.imwrite(outdir + filename[i])





# get Landmark














# # Lord an color image in grayscale
# # img = cv2.imread('../images/ibug-300w/indoor_001.png', 0)
# img = cv2.imread(indir + filename[i])

# # Draw a circle
# # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
# # cv2.circle(img, (446, 91), 5, (3,198,2), 1)

# ## prepare location for rendering dots
# # dot_location = open('/Users/chihiro/Documents/08.Jolie-Joli/Images/ibug/300W/out_indoor/indoor_001.txt').read().split("\n")[0:-1]






# # Display an image
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.imwrite('../images/ibug-300w-circle/indoor_001_circle.png',img)
# cv2.destroyAllWindows()


#         cv2.putText(img, str(i+1), (dot_location[i][0], dot_location[i][1]), font, 0.3, (3,198,2), 2, cv2.LINE_AA)
