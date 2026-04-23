import cv2 as cv

#Task Two Read and Show Image in One Command:

img = cv.imshow('Frog', cv.imread('images/blue_frog.jpg'))

cv.waitKey(0) 