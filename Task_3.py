import cv2 as cv

#Task Three Convert to Gray: 

img = cv.imread('images/telephone.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
#y = 0.299 R + 0.587 G + 0.114 B
gray_img_3ch = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR ) 
#convert the gray image into 3 channels shape so that we can concatenate the original image and the gray one
print(gray_img_3ch.shape)
concatenation = cv.hconcat([img,gray_img_3ch]) 

#cv.imshow('Telephone', img)
#cv.imshow('Gray Telephone', gray_img)
cv.imshow('Telephone Concatenation', concatenation)

cv.waitKey(0)  