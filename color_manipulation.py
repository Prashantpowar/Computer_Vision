import cv2 as cv
import numpy as np

#read image
img = cv.imread('parrot.jpg')
print(img.shape)

#resize image
img1 = cv.resize(img,(1080,860))


#bgr to hsv conversion
img2 =cv.cvtColor(img1,cv.COLOR_BGR2HSV)

#array of low green channel
low_green = np.array((36,0,0))
#array of high green channel
high_green = np.array((86,255,255))

#masking within range of low and high green channel
green_mask = cv.inRange(img2, low_green, high_green)

#adding images and mask to show green color
green = cv.bitwise_and(img1, img1, mask = green_mask)


cv.imshow("image",green)
# cv.imwrite('green.png',green)
cv.waitKey(0)
cv.destroyAllWindows()