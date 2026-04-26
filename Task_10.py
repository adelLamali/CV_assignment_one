import cv2 as cv

#Task ten Crop an Image:

img = cv.imread('images/leaf.jpg')
image_height = img.shape[0]
image_width = img.shape[1]
#crop the image in order to focus on the leaf and keep it the center.
cropped_image = img[50:560,120:355]
#resize the cropped image so that it can be concatenated with the original one.
resized_cropped_image = cv.resize(cropped_image,(image_width,image_height))

concatenation = cv.hconcat([img, resized_cropped_image]) 

cv.imshow('resized cropped leaf concatenation',concatenation)
cv.waitKey(0) 