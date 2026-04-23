import cv2 as cv
import numpy as np

#Task Six Add Gaussian Noise to Image:

img = cv.imread('images/car.jpg')

height = img.shape[0]
width = img.shape[1]
# 1. Create a noise array with the same shape and type as the image
# We use np.zeros_like or np.zeros to ensure dimensions match
noise = np.zeros(img.shape, np.int16) 

gaussian_noise = cv.randn(noise, 0, 15)

# Add the noise to the original image
# We convert to int16/int32 first to prevent wrap-around (overflow) 
# and then clip the results to [0, 255]
img_filtered = cv.add(img,gaussian_noise,dtype=cv.CV_8U)
#gaussian_filter = cv.GaussianBlur(img,noise, 15 )

cv.imshow('Car',img)
cv.imshow('Filtered Car',img_filtered)

cv.waitKey(0)
