import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#Read the image using OpenCV.
img = cv.imread("coins.jpg")

cv.imshow('sample_image',img)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
cv.imshow('thresh_img',thresh)
cv.waitKey(0)
cv.destroyAllWindows()
#noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

#sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)

#finding sure foreground area
dist_transform=cv.distanceTransform(opening, cv.DIST_L2,5)

ret,sure_fg=cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

#finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_fg, sure_bg)

cv.imshow('unknown_img',sure_bg)
cv.imshow('unknown_img',sure_fg)
cv.waitKey(0)
cv.destroyAllWindows()
#marker labeling
ret, markers = cv.connectedComponents(sure_fg)
#add one at all labels so that sure background is not 0, but 1
markers = markers+1
#now, mark the region of the unknown with 0
markers[unknown==255] = 0
cv.imshow('makers_img', ret)
cv.waitKey(0)
cv.destroyAllWindows()