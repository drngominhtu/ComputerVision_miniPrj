import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('image3.png', 0)
img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(img, 40, 100) #minVal, maxVal

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(edge, cmap='gray') 
plt.show()
