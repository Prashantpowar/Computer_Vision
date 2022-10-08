import cv2 as cv
import numpy as np


#image reading

img1 = cv.imread("cropped_image.jpeg")
img2 = cv.imread("cropped_image.jpeg")
img3 = cv.imread("cropped_image.jpeg")
img4 = cv.imread("cropped_image.jpeg")

#image resizing
img1 = cv.resize(img1,(200,200))
img2 = cv.resize(img1,(200,200))
img3 = cv.resize(img1,(200,200))
img4 = cv.resize(img1,(200,200))

#image horizontal stacking

horizontal_image1 = np.hstack((img1,img2))
horizontal_image2 = np.hstack((img3,img4))

#image vertical stacking

vertical_stack = np.vstack((horizontal_image1,horizontal_image2))

# to show the image
cv.imshow("image",vertical_stack)

#to save the file
cv.imwrite("stacked.jpg",vertical_stack)


cv.waitKey(0)
cv.destroyAllWindows()
