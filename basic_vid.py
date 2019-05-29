import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#inorder to save output file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('images/output.avi', fourcc, 20.0, (640,480))

while True:
	ret, frame = cap.read()
	#change video color
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('gray', gray)
	#show original video aside as well
	cv2.imshow('frame', frame)
	out.write(frame)
	if cv2.waitKey(1)  & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv2.destroyAllWindows()