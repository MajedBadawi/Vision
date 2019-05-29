import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an color image in: grayscale (0) || colored (1) || unchanged (-1)
image = cv2.imread("images/basic.png", 0)

# show the image by passing the title and path
cv2.imshow("image", image)

# wait for any key to be pressed, then close windows and save image
k = cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/changed.png',image)

#add matplot lib and axes
plt.imshow(image, cmap='gray', interpolation='bicubic')
plt.plot([50,100], [80,100], 'c', linewidth=5) #draw line on the picture
plt.show()