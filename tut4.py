import numpy as np
import cv2

# load the image using OpenCV
ImageA = cv2.imread('lena.tiff', cv2.IMREAD_UNCHANGED)
# IMREAD_UCHANGED ensures that the image is loaded as is
#(including alpha chanelif it exists)

# check the dimensions of Imagea