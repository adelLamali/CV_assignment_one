import cv2 as cv
from Task_7 import blend

img1 = cv.imread('images/cherries.jpg')
img2 = cv.imread('images/coffee_beans.jpg')

#resise to make sure that they have same size
img2 = cv.resize(img2,(img1.shape[1],img1.shape[0]))

alpha = 0.75
blend(img1,img2,alpha)
