import cv2 as cv
#from PIL import Image


#image reading
image = cv.imread("832110000000.jpeg")

#to show shape of image
print(image.shape)

#print(image2.shape)


#to resize the image
#image3 = cv.resize(image,(480,640))
#0,200        250,400

#to crop the image
crop_image = image[0:250, 200:400]
print(crop_image.shape)

#print(image3.shape)
cv.imwrite('cropped_image.jpeg',crop_image)
#00 200,300


#to paste one image on another
image[0:250,0:200] =crop_image

#to save the file
cv.imwrite("pasted1.jpg",image)

#to show image
cv.imshow("img",image)
cv.waitKey(0)

cv.destroyAllWindows()
