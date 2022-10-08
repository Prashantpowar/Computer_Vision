import cv2 as cv
import numpy as np


img = cv.imread('laser.png')
print('size of img ',img.shape)
#100,100   1900,1000
crop_image=img[100:1000,100:1900]

print(crop_image.shape)


#500,180   900,500
# crop_image[500:900,180:500,2] = crop_image[500:900,180:500,0]
#BGR values
#white 255,255,255| black 0,0,0
# img1[:,:,0],img1[:,:,1],img1[:,:,2]=16,180,20

crop_image[180:500:2,500:900:2,0]=0
crop_image[180:500:2,500:900:2,1]=0
crop_image[180:500:2,500:900:2,2]=0





cv.imshow("image",crop_image)
cv.waitKey(0)
cv.destroyAllWindows()

