import cv2  
import numpy as np  

def apply_sharpen_kernel(image):
    # Tạo sharpen kernel
    kernel = [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
    
    height, width = image.shape[0], image.shape[1]
    
    # Tạo ảnh đầu ra
    output = np.zeros((height, width), dtype=np.uint8)
    
    # hàm tích chập
    for y in range(1, height-1):
        for x in range(1, width-1):
            sum = 0
            
            # Áp dụng kernel 3x3
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    pixel = image[y + ky, x + kx]
                    k_value = kernel[ky + 1][kx + 1]
                    sum += pixel * k_value
            
            # Giới hạn giá trị trong khoảng [0, 255]
            output[y, x] = max(0, min(255, sum))
    
    return output
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def main():
    # Đọc ảnh và chuyển sang ảnh xám
    image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Áp dụng sharpen kernel
    sharpened = apply_sharpen_kernel(image)
    
    # Hiển thị kết quả
    cv2.imshow('Original', image)
    cv2.imshow('Sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()