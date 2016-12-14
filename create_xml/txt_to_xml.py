# -*- coding: utf-8 -*-
# root = dir

import numpy as np

## 変数の準備
dir_in = "01_Indoor/"
dir_out = "02_Outdoor/"

## file_nameのファイルを作る
fn_in   = open("filenames.txt").read().split("\n")
fn_out  = open("filenames.txt").read().split("\n")

## txtを読み込む
txtdat_in  = [0] * 300
txtdat_out = [0] * 300
num_file   = len(fn_in)

for i in range(num_file):
    landmarks = open( dir_in + fn_in[i] ).read().split("\n")
    txtdat_in[i] = landmarks[3:-2]


### str -> float -> round -> int -> str
#### str -> round -> int
# まずは分解
eachdat = txtdat_in
i=j=0
for i in range(len(txtdat_in)):
    for j in range(len(txtdat_in[i])):
        eachdat[i][j] = txtdat_in[i][j].split(" ")

i=j=0
for i in range(len(eachdat)):
    for j in range(len(eachdat[i])):
        eachdat[i][j][0] = str(int(np.round(float(eachdat[i][j][0]))))
        eachdat[i][j][1] = str(int(np.round(float(eachdat[i][j][1]))))

#### int -> str
i=j=0
for i in range(len(eachdat)):
    for j in range(len(eachdat[i])):
        if j < 10 :
            eachdat[i][j] = "      <part name='0" + str(j) + "' x='" + eachdat[i][j][0] + "' y='" + eachdat[i][j][1] + "'/>"
        else:
            eachdat[i][j] = "      <part name='" + str(j) + "' x='" + eachdat[i][j][0] + "' y='" + eachdat[i][j][1] + "'/>"



out = open("out.txt", 'wt')
out.write("\n".join(eachdat[0]))
out.close