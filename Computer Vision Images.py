import cv2
import numpy as np
from uwimg import *


#Taking input from a directory path
img = cv2.imread('old.jpg',0)
#Applying Histogram Equalization
equ = cv2.equalizeHist(img)
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, row, col, 0, 0)
#Save the image
cv2.imwrite('new.png',equ)
