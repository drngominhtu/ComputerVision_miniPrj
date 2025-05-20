import cv2 
import numpy as np

def classify_phone_mouse(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Use Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)
    
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Initialize variables to count phone and mouse
    phone_count = 0
    mouse_count = 0
    
    for contour in contours:
        # Calculate the area of each contour
        area = cv2.contourArea(contour)
        
        if area > 1000:  # Filter out small contours
            # Get the bounding rectangle for the contour
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h
            
            # Classify based on aspect ratio and area
            if aspect_ratio > 1.5 and area > 20000:  # Phone-like shape
                phone_count += 1
            elif aspect_ratio < 1.5 and area < 20000:  # Mouse-like shape
                mouse_count += 1
    
    return phone_count, mouse_count