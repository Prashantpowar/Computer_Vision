import cv2 as cv
import numpy as np

img = cv.imread("parrot.jpg")
img1 = cv.resize(img,(1080,860))

b,g,r = img1[40,50]

print(b,g,r)



cv.imshow("image",img1)
cv.waitKey()
cv.destroyAllWindows()


