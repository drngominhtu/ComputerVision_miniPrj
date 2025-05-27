import cv2
import numpy as np

def edge_detect(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    #GaussianBlur
    blurred = cv2.GaussianBlur(img, (5,5), 0)

    # Canny edge detection
    edges = cv2.Canny(blurred, threshold1=30, threshold2=150)
    
    # Áp dụng phép dãn (dilation) để làm rõ cạnh
    kernel = np.ones((5,5), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)
    
    return dilated_edges, img



def classify_contour(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    # Tính độ tròn (circularity)
    circularity = 4 * np.pi * area / (perimeter * perimeter) if perimeter > 0 else 0

    epsilon = 0.04 * perimeter
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Số đỉnh của đa giác xấp xỉ
    vertices = len(approx)

    # classify based on circularity and number of vertices =====================================================================================
    if circularity > 0.7 or (circularity > 0.6 and vertices > 8):
        # Hình dạng tròn, khả năng cao là chuột
        return "mouse"
    elif vertices >= 4 and vertices <= 6 and circularity < 0.3:
        # Hình dạng chữ nhật/vuông, khả năng cao là điện thoại
        return "phone"
    else:
        # Phân loại dựa trên độ tròn nếu không chắc chắn
        return "mouse" if circularity > 0.7 else "phone"
    #========================================================================================================================


def process_image(image_path, output_path=None):
    # Tính toán contour
    edges, img = edge_detect(image_path)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # filter
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]
    
    # Tạo bản sao để vẽ lên
    result_img = img.copy()
    
    # Xử lý từng contour
    for contour in filtered_contours:
        # Phân loại contour
        prediction = classify_contour(contour)
        
        # Chọn màu border tùy theo loại
        color = (0, 255, 0) if prediction == "phone" else (0, 0, 255)
        
        # Vẽ contour với màu đã chọn, độ dày 3 pixel
        cv2.drawContours(result_img, [contour], -1, color, 3)
        
        # Tính toán bounding box
        x, y, w, h = cv2.boundingRect(contour)
        
        # Vẽ bounding box
        cv2.rectangle(result_img, (x, y), (x+w, y+h), color, 2)
        
        # Chuẩn bị label và vẽ
        label = prediction.upper()
        label_y = max(y - 10, 20)
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        cv2.rectangle(result_img, (x, label_y - label_size[1] - 10), 
                    (x + label_size[0] + 10, label_y), color, -1)
        cv2.putText(result_img, label, (x + 5, label_y - 5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # # Lưu ảnh kết quả nếu đường dẫn output được cung cấp
    # if output_path:
    #     cv2.imwrite(output_path, result_img)
    
    return result_img



def main():
    # Đường dẫn đến ảnh cần phân loại
    image_path = "data/img3.jpg"
    output_path = "output_classification.jpg"
    
    # Xử lý ảnh
    result = process_image(image_path, output_path)
    
    # Hiển thị kết quả
    height, width = result.shape[:2]
    scale_factor = min(1.0, 1000 / max(height, width))  # Tối đa 800px
    
    result_resized = cv2.resize(result, (0, 0), fx=scale_factor, fy=scale_factor)
    cv2.imshow('Classification Result', result_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()