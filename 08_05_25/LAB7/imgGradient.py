import numpy as np  
import cv2 as cv   
from matplotlib import pyplot as plt  # Thư viện để hiển thị ảnh

# Đọc ảnh và chuyển sang ảnh xám
img = cv.imread('sample.JPG', cv.IMREAD_GRAYSCALE)  # Đọc ảnh dưới dạng grayscale
# Tính toán đạo hàm Sobel theo hướng x với đầu ra 8-bit
sobelx8u = cv.Sobel(img,        # Ảnh đầu vào
                    cv.CV_8U,    # Độ sâu bit đầu ra (8-bit unsigned)
                    1,           # Bậc đạo hàm theo x
                    0,           # Bậc đạo hàm theo y
                    ksize=5)     # Kích thước kernel Sobel (5x5)

# Tính toán đạo hàm Sobel với độ chính xác cao hơn (64-bit)
sobelx64f = cv.Sobel(img,       # Ảnh đầu vào
                     cv.CV_64F,  # Độ sâu bit đầu ra (64-bit float)
                     1,          # Bậc đạo hàm theo x
                     0,          # Bậc đạo hàm theo y
                     ksize=5)    # Kích thước kernel Sobel (5x5)
abs_sobel64f = np.absolute(sobelx64f)  # Lấy giá trị tuyệt đối của đạo hàm Sobel
sobel_8u = np.uint8(abs_sobel64f)      # Chuyển đổi sang 8-bit unsigned

# Hiển thị ảnh gốc và các ảnh sau khi tính toán đạo hàm Sobel
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()