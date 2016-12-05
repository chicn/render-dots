# -*- coding: utf-8 -*-

import numpy as np
import pdb

# print "Please type some words to input"
# input_lines = raw_input()
# print input_lines


print "Please type the PATH of the directory which contains images."
imdir = raw_input() + "/"

print "Please type the file name which contains the list of file names."
fn = raw_input()
fn = open(imdir + "/" + fn).read().split("\n")


#txtを読み込む
txtdat = [0] * 300
# num_file = len(fn)

for i in range(len(fn)):
    landmarks = open (imdir + fn[i]).read().split("\n")
    txtdat[i] = landmarks[3:-2]

# split to x and y
eachdat = txtdat
i = j = 0
for i in range(len(txtdat)):
    for j in range(len(txtdat[i])):
        eachdat[i][j] = txtdat[i][j].split(" ")

# str -> int(round)

i = j = 0
for i in range(len(eachdat)):
    for j in range(len(eachdat[i])):
        eachdat[i][j][0] = str(int(np.round(float(eachdat[i][j][0]))))
        eachdat[i][j][1] = str(int(np.round(float(eachdat[i][j][1]))))

for i in range(len(eachdat)):
    for j in range(len(eachdat[i])):
        eachdat[i][j] = str(eachdat[i][j][0]) + ", " + str(eachdat[i][j][1]) + "\n"


a = [0] * len(eachdat)
for i in range(len(eachdat)):
    for j in range(len(eachdat[i])):
        if j < 1 :
            a[i] = str(eachdat[i][j])
        else:
            a[i] = a[i] + str(eachdat[i][j])



print "Type a directory to put all outputs"
out_dir = raw_input() + "/"
for i in range(len(eachdat)):
    f = open(out_dir + fn[i], 'w')
    f.write(str(a[i]))
    f.close