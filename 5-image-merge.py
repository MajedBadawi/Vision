import cv2
import numpy as numpy

#load two images of same size
image1 = cv2.imread('images/merge1.png', 1)
image2 = cv2.imread('images/merge2.png', 1)

#merge two images
#add = image1 + image2
add = cv2.addWeighted(image1, 0.6, image2, 0.4, 0)

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()
