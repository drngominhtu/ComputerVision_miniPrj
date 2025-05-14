import cv2 as cv
import numpy as np

im = cv.imread('image3.png')

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 33, 255, cv.THRESH_BINARY)

contour,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im, contour, -1, (0, 255, 0), 3)  #cv.drawContours(image, contours[outline], contourIdx, color, thickness)

cv.imshow('Contours', im)
cv.waitKey(0)
cv.destroyAllWindows()