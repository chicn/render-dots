# -*- coding: utf-8 -*-
import cv2
import glob

print("グレーに変換したい画像が入ったディレクトリを指定してください")
img_dir = raw_input()
if img_dir[-1] != '/':
    img_dir += '/'

print("グレーに変換したい画像を出力したいディレクトリを指定してください")
out_dir = raw_input()
if out_dir[-1] != '/':
    out_dir += '/'


img_names = glob.glob(img_dir + '*')
img_names_simple  = []

for i, img_name in enumerate(img_names):
    slash_index = img_name.rfind('/')
    img_names_simple.append(img_name[slash_index+1:])

i = 0
if len(img_names) != len(img_names_simple):
    print("Warning: \"img_names\" and \"img_names_simple\" don't match")
    # break


i = 0
for i in range(len(img_names_simple)):
    img = img_names_simple[i]
    if '.png' not in img:
        if '.jpeg' not in img:
            if 'jpg' not in img:
                img_names.pop(i)
                img_names_simple.pop(i)

i = 0
for i in range(len(img_names)):
    slash_index = img_names[i].rfind('/')
    a = img_names[i][slash_index+1:]
    if a != img_names_simple[i]:
        print("Warning: %s and %s don't match." % (img_names[i], img_names_simple[i]))
        break


i = 0
for i, img_name in enumerate(img_names):
    print("Writing: %s" img_names_simple[i])
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(out_dir + img_names_simple[i], gray)


print("Finished Saving!!")
