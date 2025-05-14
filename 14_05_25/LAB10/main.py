import cv2 as cv
import numpy as np

im = cv.imread('image.png')

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
contour,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im, contour, -1, (0, 255, 0), 3)
cv.imshow('Contours', im)