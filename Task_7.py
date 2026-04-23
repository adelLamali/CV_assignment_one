import cv2 as cv
import numpy as np


def blend(a,b,alpha):

    #blends two images a and b with a given blending factor alpha:
    #result = α · a + (1 − α) · b
    result =  alpha * a.astype(float)  + ( 1 - alpha) * b.astype(float)

    #convert back to uint8
    blended = np.clip(result, 0, 255).astype(np.uint8)

    cv.imshow('Blended images',blended)
    cv.waitKey(0)


