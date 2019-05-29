import cv2
import numpy as np

image = cv2.imread('images/basic.png', 1)

#draw line from point to another with a specific color (in bgr) and width
cv2.line(image, (0,0), (150,150), (0,255,255), 15)

#draw rectangle as before
cv2.rectangle(image, (15,25), (200,150), (255,0,0), 5)

#draw a cricle with center, radius and color with fillin (-1)
cv2.circle(image, (100,63), 55, (0,0,255), -1)

#draw a polygon
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image, [pts], True, (0,0,0), 3)

#add text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello World', (0,130), font, 1, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()