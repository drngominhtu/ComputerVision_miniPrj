import cv2
import numpy as np

# Load ảnh gốc
img = cv2.imread('sample.jpg')

# Sharpen kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

# Áp dụng filter
sharpened = cv2.filter2D(img, 0, kernel)

# Hiển thị
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
