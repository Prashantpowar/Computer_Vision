import numpy as np
import cv2 as cv


#creating blank image of 4000*4000 shape
img = np.zeros((4000,4000,3), dtype=np.uint8)

#image resizing
img1 =cv.resize(img,(640,640))



#cv.imwrite("blank_image1.jpeg", img)
global x1, y1, x2, y2
x1 = 5
y1 = 5
x2 = 100
y2 = 50

#loop for y coordinates
for i in range(8):
	# print('in loop of y')
	# print('y1',y1)
	# print('y2',y2)
	# print('x1',x1)
	# print('x2',x2)
	x1 = 5
	x2 = 100
	

	#rectangle on image
	# img2 = cv.rectangle(img1,(x1,y1),(x2,y2),(255,255,0),2)

	#loop for x coordinates direction
	for i in range(5):
		# print('in loop of x')
		# print('y1',y1)
		# print('y2',y2)
		# print('x1',x1)
		# print('x2',x2)

		#rectangle on image
		img2 = cv.rectangle(img1,(x1,y1),(x2,y2),(0,255,255),2)
		x1 = x1 + 130
		x2 = x2 + 130
	y1 = y1 +80
	y2 = y2 +80
	

	

cv.imwrite("imag.jpeg",img2)
cv.imshow("image",img2)
	

#wait until key pressed
cv.waitKey(0)

cv.destroyAllWindows()
