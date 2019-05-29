import cv2
import numpy as numpy

#load two images of same size
image = cv2.imread('images/logo.png', 1)

rows, cols, channels = image.shape
roi = image[0:rows, 0:cols]

img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold (img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

cv2.waitKey(0)
cv2.destroyAllWindows()