import cv2 as cv

#Task One Load and Display Image:
img = cv.imread('images/car.jpg')

cv.imshow('Car', img) 

width = img.shape
height = img.shape[0]
channels = img.shape[2]
dtype = img.dtype

print("Width = ",width)
print("Height = ",height)
print("Channels = ",channels)
print("Data type = ",dtype)

cv.waitKey(0)