import numpy as np
import cv2
from matplotlib import pyplot as plt

# Đọc ảnh
img = cv2.imread('image2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tiền xử lý: làm mịn ảnh để loại bỏ nhiễu
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Phân ngưỡng theo thuật toán Otsu để lấy mask thô
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Phép toán morphology để loại bỏ nhiễu và tách các đối tượng dính nhau
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Xác định vùng chắc chắn thuộc nền
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Xác định vùng chắc chắn thuộc đối tượng bằng distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# Xác định vùng không chắc chắn
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Đánh nhãn các marker
ret, markers = cv2.connectedComponents(sure_fg)
# Tăng tất cả nhãn lên 1 để bảo đảm nền không phải là 0
markers = markers + 1
# Đánh dấu vùng không chắc chắn là 0
markers[unknown == 255] = 0

# Áp dụng watershed
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]  # Đánh dấu đường biên bằng màu đỏ

# Hiển thị kết quả
plt.figure(figsize=(12, 8))
plt.subplot(231), plt.imshow(gray, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(232), plt.imshow(thresh, cmap='gray'), plt.title('Phân ngưỡng')
plt.subplot(233), plt.imshow(sure_bg, cmap='gray'), plt.title('Vùng nền chắc chắn')
plt.subplot(234), plt.imshow(dist_transform, cmap='jet'), plt.title('Distance Transform')
plt.subplot(235), plt.imshow(sure_fg, cmap='gray'), plt.title('Vùng đối tượng chắc chắn')
plt.subplot(236), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Kết quả')
plt.tight_layout()
plt.show()