# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 23:10:05 2019

@author: ASUS
"""

from PIL import Image
import numpy as np

def load_image(infilename):
    img= Image.open(infilename)
    data = np.asarray(img, dtype = "int32")
    return data

data = load_image("2.jpg")

print(data)