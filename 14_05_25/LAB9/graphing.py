import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tạo ảnh mẫu thay vì đọc file
def create_sample_image(size=100):
    img = np.zeros((size, size), dtype=np.uint8)
    
    # Vẽ hình tròn chính
    cv2.circle(img, (50, 50), 20, 255, -1)
    
    # Thêm một số nhiễu
    for _ in range(50):
        x, y = np.random.randint(0, size, 2)
        img[y, x] = 255
        
    return img

# Sử dụng ảnh mẫu thay vì đọc file
img = create_sample_image()

# Hàm đếm pixel trắng
def count_white_pixels(img):
    return np.sum(img > 0)

# Hàm tính toán profile cho mỗi dòng
def calculate_row_profile(img):
    return np.sum(img > 0, axis=1)

# Tạo kernel với kích thước khác nhau
results = {}
iterations = 10
sizes = [3, 5, 7, 9, 11]

# Tính toán và lưu kết quả cho từng loại biến đổi với nhiều kích thước kernel và số lần lặp
for size in sizes:
    kernel = np.ones((size, size), np.uint8)
    
    # Khởi tạo danh sách cho mỗi phép biến đổi
    erosion_counts = []
    dilation_counts = []
    opening_counts = []
    closing_counts = []
    gradient_counts = []
    tophat_counts = []
    blackhat_counts = []
    
    # Thực hiện với nhiều iterations
    for i in range(iterations):
        if i == 0:
            # Iteration 0: ảnh gốc
            erosion_counts.append(count_white_pixels(img))
            dilation_counts.append(count_white_pixels(img))
            opening_counts.append(count_white_pixels(img))
            closing_counts.append(count_white_pixels(img))
            gradient_counts.append(0)  # Gradient của ảnh gốc với chính nó là 0
            tophat_counts.append(0)    # Top hat của ảnh gốc là 0
            blackhat_counts.append(0)  # Black hat của ảnh gốc là 0
        else:
            # Áp dụng các phép biến đổi với i lần lặp
            erosion = cv2.erode(img, kernel, iterations=i)
            dilation = cv2.dilate(img, kernel, iterations=i)
            opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=i)
            closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=i)
            gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=i)
            tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=i)
            blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=i)
            
            # Đếm số pixel trắng
            erosion_counts.append(count_white_pixels(erosion))
            dilation_counts.append(count_white_pixels(dilation))
            opening_counts.append(count_white_pixels(opening))
            closing_counts.append(count_white_pixels(closing))
            gradient_counts.append(count_white_pixels(gradient))
            tophat_counts.append(count_white_pixels(tophat))
            blackhat_counts.append(count_white_pixels(blackhat))
    
    # Lưu kết quả cho kích thước kernel này
    results[size] = {
        'erosion': erosion_counts,
        'dilation': dilation_counts,
        'opening': opening_counts,
        'closing': closing_counts,
        'gradient': gradient_counts,
        'tophat': tophat_counts,
        'blackhat': blackhat_counts
    }

# Vẽ biểu đồ cho mỗi phép biến đổi
plt.figure(figsize=(15, 15))

operations = ['erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'blackhat']
titles = ['Erosion (Co)', 'Dilation (Giãn)', 'Opening (Mở)', 'Closing (Đóng)', 
          'Gradient (Biên)', 'Top Hat (Chi tiết sáng)', 'Black Hat (Chi tiết tối)']
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'black']

for idx, op in enumerate(operations):
    plt.subplot(4, 2, idx+1)
    for size in sizes:
        plt.plot(range(iterations), results[size][op], 
                 label=f'Kernel {size}x{size}', 
                 marker='o', linewidth=2)
    plt.title(titles[idx], fontsize=14)
    plt.xlabel('Số lần lặp (iterations)', fontsize=12)
    plt.ylabel('Số pixel trắng', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

plt.tight_layout()
plt.suptitle("Biểu đồ khảo sát các phép biến đổi hình thái học", fontsize=16)
plt.subplots_adjust(top=0.92)
plt.savefig('morphology_line_charts.png', dpi=300, bbox_inches='tight')
plt.show()

# Vẽ biểu đồ so sánh tất cả các phép biến đổi với một kích thước kernel
plt.figure(figsize=(12, 6))
size = 5  # Chọn kernel 5x5

for idx, op in enumerate(operations):
    plt.plot(range(iterations), results[size][op], 
             label=titles[idx], 
             color=colors[idx],
             marker='o', linewidth=2)

plt.title(f"So sánh các phép biến đổi hình thái học với kernel {size}x{size}", fontsize=14)
plt.xlabel('Số lần lặp (iterations)', fontsize=12)
plt.ylabel('Số pixel trắng', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('morphology_comparison.png', dpi=300)
plt.show()