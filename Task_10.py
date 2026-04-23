import cv2 as cv

#Task ten Crop an Image:

img = cv.imread('images/leaf.jpg')
image_height = img.shape[0]
image_width = img.shape[1]

cropped_image = img[50:560,120:355]

resized_cropped_image = cv.resize(cropped_image,(image_width,image_height))

concatenation = cv.hconcat([img, resized_cropped_image]) 

#cv.imshow('leaf',img)
#cv.imshow('cropped leaf',cropped_image)
#cv.imshow('resized cropped leaf',resized_cropped_image)
cv.imshow('resized cropped leaf concatenation',concatenation)
cv.waitKey(0) 