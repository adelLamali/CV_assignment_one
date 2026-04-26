import cv2 as cv
import numpy as np

#Task eleven Crop an Image:

img = cv.imread('images/window.jpg')
#y = 0.299 R + 0.587 G + 0.114 B
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY )

#Averaging filter
averaging_filter = cv.blur(gray_img,(5,5))

#Gaussian filter
gaussian_filter = cv.GaussianBlur(gray_img,(5,5), 1 )

#The difference between the two filtered results
diff = cv.absdiff(averaging_filter,gaussian_filter)

#Apply a suitable Colormap
#colored_diff = cv.applyColorMap(diff,cv.COLORMAP_COOL)

top = np.hstack((gray_img,averaging_filter))
bottom = np.hstack((gaussian_filter,diff))
grid = np.vstack((top,bottom))
cv.imshow('grid window',grid)
cv.waitKey(0)