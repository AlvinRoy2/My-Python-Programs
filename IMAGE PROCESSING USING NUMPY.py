# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:11:46 2022

@author: HP
"""

import numpy as np
from PIL import Image
im=Image.open("Bird.png")

#Loading an Image
pixelmap=im.load()

#Matrix Form
#I=np.asarray(Image.open("Bird.png"))

img=Image.new(im.mode,im.size)

pixelnew=img.load()

'''
Converting into 3 bit image
which takes value from 0 to 7
0-31 =0
32-63 =1
64-95 =2
96-127=3
128-159=4
160-191=5
191-223=6
224-255=7

'''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixelmap[i,j]>=0 and pixelmap[i,j]<=31):
            pixelnew[i,j]=0
        elif (pixelmap[i,j]>=32 and pixelmap[i,j]<=63):
            pixelnew[i,j]=1
        elif (pixelmap[i,j]>=64 and pixelmap[i,j]<=95):
            pixelnew[i,j]=2
        elif (pixelmap[i,j]>=96 and pixelmap[i,j]<=127):
            pixelnew[i,j]=3
        elif (pixelmap[i,j]>=128 and pixelmap[i,j]<=159):
            pixelnew[i,j]=4
        elif (pixelmap[i,j]>=160 and pixelmap[i,j]<=191):
            pixelnew[i,j]=5
        elif (pixelmap[i,j]>=192 and pixelmap[i,j]<=223):
            pixelnew[i,j]=6
        elif (pixelmap[i,j]>=224 and pixelmap[i,j]<=255):
            pixelnew[i,j]=7
            
img.save('BIRD.png')
#Loading the new Image
#J=np.asarray(Image.open('BIRD.png'))

            
            
            
            