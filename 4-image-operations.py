import cv2
import numpy as numpy

image = cv2.imread('images/basic.png', 1)

#get a specific pixel
px = image[55,55]
#change value of a pixel
#image[55,55] = [255,255,255]

#change roi: region of image (part of the image)
image[100:150, 100:150] = [255,255,255]

#duplicate part of the image
part = image[37:111, 107:194]
image[0:74, 0:87] = part

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()