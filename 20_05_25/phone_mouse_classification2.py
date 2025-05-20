import cv2
import numpy as np
from sklearn.cluster import KMeans

def edge_detect(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)
    
    # Tiền xử lý ảnh: chuyển đổi sang grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Tối ưu các pixel bằng GaussianBlur
    blurred = cv2.GaussianBlur(gray_img, (5,5), 0)
    
    # Canny edge detection
    edges = cv2.Canny(blurred, threshold1=30, threshold2=150)
    
    return edges

def classify_image(image_path):
    # Tính toán contour
    edges = edge_detect(image_path)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tách các contour theo kích thước và hình dạng
    features = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        features.append([x, y, w, h, area, perimeter])

    # Clustering
    kmeans = KMeans(n_clusters=2)  # Chia thành 2 nhóm
    labels = kmeans.fit_predict(features)

    # Xozeo dự đoán
    if labels[0] == 0:
        return "phone"
    else:
        return "mouse"

def show_result(image_path, prediction):
    img = cv2.imread(image_path)  # Đọc ảnh từ đường dẫn được cung cấp
    edges = edge_detect(image_path)

    # Tìm contours từ edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sắp xếp contours theo diện tích (lớn nhất trước)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # Lọc contours quá nhỏ
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]
    
    # Vẽ tất cả contours lên ảnh với màu khác nhau
    img_copy = img.copy()
    for i, cnt in enumerate(filtered_contours[:5]):  # Chỉ vẽ 5 contours lớn nhất
        color = (0, 255, 0) if i == 0 else (0, 0, 255)  # Contour lớn nhất màu xanh lá
        cv2.drawContours(img_copy, [cnt], -1, color, 2)
        
        # Tính toán và hiển thị đặc trưng
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h
        area = cv2.contourArea(cnt)
        
        # Hiển thị thông tin
        text = f"AR: {aspect_ratio:.2f}, Area: {area}"
        cv2.putText(img_copy, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
    # Hiển thị kết quả phân loại
    result_text = f"Kết quả: {prediction.upper()}"
    cv2.putText(img_copy, result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    # Hiển thị ảnh với contours
    cv2.imshow('Classification Result', img_copy)
    
    # Hiển thị ảnh edge
    cv2.imshow('Edge Detection', edges)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Đường dẫn đến ảnh cần phân loại
    image_path = "img7.jpg"  # Thay đổi tên file ảnh tại đây
    
    # Phân loại ảnh
    prediction = classify_image(image_path)
    
    # Hiển thị kết quả
    print(f"Kết quả phân loại: {prediction}")
    
    # Hiển thị ảnh với contour được đánh dấu
    show_result(image_path, 0 if prediction == "phone" else 1)

# Chạy chương trình khi file được thực thi trực tiếp
if __name__ == "__main__":
    main()


