# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:27:09 2020

@author: PaulJ
"""

import os
import PIL

filenames = []

# basepath = '~/images'
basepath = './images'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            filenames.append(entry)

for a_fn in filenames:
    # fn_base = ''.join(a_fn.split('.')[:-1])
    # img = PIL.Image('~/images/' + a_fn.name)
    img = PIL.Image.open('./images/' + a_fn.name)
    new_img = img.rotate(270).resize((7000, 3600))
    # new_img.save('/opt/icons/' + a_fn)
    new_img.save('./new_images/' + a_fn.name)




#!/usr/bin/env python3

from PIL import Image
import os


img_path = 'supplier-data/images/'
filenames = os.scandir(img_path)

for a_fn_obj in filenames:
    a_fn = a_fn_obj.name
    if not a_fn.endswith('.tiff'):
        continue
    img_base = a_fn.split('.')[0]
    img = Image.open(img_path + a_fn)
    img = img.convert(mode='RGB').resize(size=(600, 400))
    img.save(img_path + img_base + '.jpeg')
