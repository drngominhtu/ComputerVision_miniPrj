import cv2 as cv
import numpy as np


img = cv.imread('image3.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Áp dụng ngưỡng
ret, thresh = cv.threshold(gray, 33, 255, cv.THRESH_BINARY)

# Tìm contour
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Vẽ tất cả contour
img_contours = img
cv.drawContours(img_contours, contours, -1, (0, 255, 0), 10)

cv.imshow('Original', img, )
cv.imshow('Threshold', thresh)
cv.imshow('Contours', img_contours)
cv.waitKey(0)
cv.destroyAllWindows()