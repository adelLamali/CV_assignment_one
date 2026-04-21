import cv2 as cv
import numpy as np
#Task One Load and Display Image:
""" img = cv.imread('images/car.jpg')

cv.imshow('Car', img)

width = img.shape[1]
height = img.shape[0]
channels = img.shape[2]
dtype = img.dtype

print("Width = ",width)
print("Height = ",height)
print("Channels = ",channels)
print("Data type = ",dtype)

cv.waitKey(0) """

#Task Two Read and Show Image in One Command:

""" img = cv.imshow('Frog', cv.imread('images/blue_frog.jpg'))

cv.waitKey(0) """

#Task Three Convert to Gray: 

""" img = cv.imread('images/telephone.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
#y = 0.299 R + 0.587 G + 0.114 B
gray_img_3ch = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR ) 
#convert the gray image into 3 channels shape so that we can concatenate the original image and the gray one
print(gray_img_3ch.shape)
concatenation = cv.hconcat([img,gray_img_3ch]) 

#cv.imshow('Telephone', img)
#cv.imshow('Gray Telephone', gray_img)
cv.imshow('Telephone Concatenation', concatenation)

cv.waitKey(0)  """

# Task Four Add Two Images:

""" img1 = cv.imread('images/cherries.jpg')
img2 = cv.imread('images/coffee_beans.jpg')

height = img1.shape[0] #Cherries image height
width = img1.shape[1] #Cherries image width
dimensions = (width,height)

img2 = cv.resize(img2,dimensions,interpolation=cv.INTER_LINEAR)
#INTER_LINEAR:It provides a good balance between speed and quality for resizing.

print('Cherries image shape',img1.shape) #Cherrie image dimensions
print('Coffee Beans image shape',img2.shape) #Coffee beans image dimensions

#Blend the two images with equal weight
blend = cv.addWeighted(img1, 0.5 ,img2, 0.5 , 0 )
#The addWeighted function here uses five parameters which are : 
#Cherries image ,Cherries image wieght between 0 and 1 lets call it "a",Coffee beans image,
# Coffee beans weight where b = 1 - a , brightness parameter added to the blended image

concatenation = cv.hconcat([img1, blend,img2]) 
cv.imshow('task 4',concatenation)

cv.waitKey() """

#Task Five Generate Gaussian Noise:

#Task Nine Colour Planes:

""" img = cv.imread('images/pool_balls.jpg')

cv.imshow('Pool Balls',img)

b,g,r = cv.split(img)

#r_plot = cv.line(r, (100,110), (150,160), (0,255,0), 30, cv.LINE_AA)
#AA means anti-alias smooth line for plot
cv.imshow('Pool Balls red color plane',r)

cv.waitKey(0) """

#Task ten Crop an Image:

""" img = cv.imread('images/leaf.jpg')
image_height = img.shape[0]
image_width = img.shape[1]

cropped_image = img[50:560,120:355]

resized_cropped_image = cv.resize(cropped_image,(image_width,image_height))

concatenation = cv.hconcat([img, resized_cropped_image]) 

#cv.imshow('leaf',img)
#cv.imshow('cropped leaf',cropped_image)
#cv.imshow('resized cropped leaf',resized_cropped_image)
cv.imshow('resized cropped leaf concatenation',concatenation)
cv.waitKey(0) """

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