import cv2
import numpy as np

img = cv2.imread('your_image.jpg')

r_hist = [0] * 256
g_hist = [0] * 256
b_hist = [0] * 256


height, width, channels = img.shape
for i in range(height):
    for j in range(width):
        b, g, r = img[i, j]
        r_hist[r] += 1
        g_hist[g] += 1
        b_hist[b] += 1

max_value = max(max(r_hist), max(g_hist), max(b_hist))


hist_height = 600
hist_width = 600
hist_image = np.zeros((hist_height, hist_width, 3), dtype=np.uint8)

# (Red)
for i in range(1, 256):
    cv2.line(hist_image, (i-1, hist_height - int(r_hist[i-1] * hist_height / max_value)),
             (i, hist_height - int(r_hist[i] * hist_height / max_value)), (0, 0, 255), 1)
# (Green)
for i in range(1, 256):
    cv2.line(hist_image, (i-1, hist_height - int(g_hist[i-1] * hist_height / max_value)),
             (i, hist_height - int(g_hist[i] * hist_height / max_value)), (0, 255, 0), 1)
#(Blue)
for i in range(1, 256):
    cv2.line(hist_image, (i-1, hist_height - int(b_hist[i-1] * hist_height / max_value)),
             (i, hist_height - int(b_hist[i] * hist_height / max_value)), (255, 0, 0), 1)


cv2.imshow('Color Histogram', hist_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
