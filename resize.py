#coding=utf-8
import numpy as np
from PIL import Image
import time
import os


def resize(srcdir, filename, dstdir):
    arr = Image.open(srcdir+filename)

    arr = arr.resize((321,321))

    arr.save(dstdir+filename)

filedir = '/Users/shenyi/Desktop/Spotweld-Dataset/00-train-original/'
dstdir = '/Users/shenyi/Desktop/Spotweld-Dataset/00-train-original-321*321/'
s = os.listdir(filedir)
s.sort()
for filename in s:
    resize(filedir, filename, dstdir)
