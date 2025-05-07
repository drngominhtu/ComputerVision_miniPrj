import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('your_image.jpg')

# Tách các kênh màu: Red, Green, Blue
r_channel = img[:, :, 2]
g_channel = img[:, :, 1]
b_channel = img[:, :, 0]

# Tính histogram cho từng kênh màu
r_hist = cv2.calcHist([r_channel], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([g_channel], [0], None, [256], [0, 256])
b_hist = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

# Tạo ảnh trắng để vẽ histogram
hist_height = 400
hist_width = 400
hist_image = np.ones((hist_height, hist_width, 3), dtype=np.uint8) * 255

# Hàm để vẽ histogram thành đường line
def draw_histogram(hist, color):
    for i in range(1, 256):
        y1 = hist_height - int(hist[i-1] * hist_height / max(hist))
        y2 = hist_height - int(hist[i] * hist_height / max(hist))
        cv2.line(hist_image, (i-1, y1), (i, y2), color, 2)

# Vẽ histogram cho từng kênh màu
draw_histogram(r_hist, (0, 0, 255))  # Đỏ
draw_histogram(g_hist, (0, 255, 0))  # Xanh lá
draw_histogram(b_hist, (255, 0, 0))  # Xanh dương

# Hiển thị kết quả
cv2.imshow('Histogram', hist_image)

# Đợi người dùng nhấn phím để đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()
