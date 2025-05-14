import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)


kernel = np.ones((5, 5), np.uint8)

# Áp dụng các phép biến đổi
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


fig, axes = plt.subplots(2, 4, figsize=(15, 8))
fig.suptitle("Các phép biến đổi hình thái học", fontsize=16)


images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
titles = ['Ảnh gốc', 'Co (Erosion)', 'Giãn (Dilation)', 'Mở (Opening)', 
          'Đóng (Closing)', 'Gradient', 'Top Hat', 'Black Hat']

schematics = [
    "Ảnh ban đầu",
    "Làm co nhỏ các đối tượng\nLoại bỏ điểm nhiễu",
    "Làm phình to các đối tượng\nLấp đầy lỗ nhỏ",
    "Erosion → Dilation\nLoại bỏ nhiễu, giữ hình dạng",
    "Dilation → Erosion\nLấp lỗ hổng, kết nối đường đứt",
    "Dilation - Erosion\nTạo biên của đối tượng",
    "Ảnh gốc - Opening\nTrích xuất chi tiết sáng nhỏ",
    "Closing - Ảnh gốc\nTrích xuất chi tiết tối nhỏ"
]

for i, ax in enumerate(axes.flat):
    if i < len(images):
        ax.imshow(images[i], cmap='gray')
        ax.set_title(titles[i])
        ax.set_xticks([])
        ax.set_yticks([])
        y_pos = -0.2 if i < 4 else 1.05
        ax.text(0.5, y_pos, schematics[i], transform=ax.transAxes, 
                ha='center', va='center', fontsize=9,
                bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.subplots_adjust(hspace=0.35, wspace=0.1)
plt.show()
