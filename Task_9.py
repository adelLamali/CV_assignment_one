import cv2 as cv


#Task Nine Colour Planes:

img = cv.imread('images/pool_balls.jpg')

cv.imshow('Pool Balls',img)

b,g,r = cv.split(img)

#r_plot = cv.line(r, (100,110), (150,160), (0,255,0), 30, cv.LINE_AA)
#AA means anti-alias smooth line for plot
cv.imshow('Pool Balls red color plane',r)

cv.waitKey(0)
