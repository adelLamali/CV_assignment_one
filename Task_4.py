import cv2 as cv


# Task Four Add Two Images:

img1 = cv.imread('images/cherries.jpg')
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

cv.waitKey()
