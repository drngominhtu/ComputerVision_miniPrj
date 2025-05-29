#histogram 
# g    | 0 1 2 3 4 5 6 7 8 9 10
# h(g) | 3 2 1 0 0 0 0 0 0 0 1

#tần suất cấp xám g là số điểm ảnh có mức xám g trong ảnh, h(g) là số điểm ảnh có giá trị bằng g

# đơn vị bin, ví dụ bin(0) với tập 0->10 là tất cả các điểm ảnh có giá trị từ 0->10

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def histogram(img):
    height, width = img.shape[:2]
    histogram = np.zeros(256, dtype=int)  # Initialize histogram with 256 bins for grayscale values

    for i in range(height):
        for j in range(width):
            pixel_value = img[i, j]
            histogram[pixel_value] += 1  # Increment the count for the pixel value

    return histogram

def plot_histogram(histogram):
    plt.figure(figsize=(10, 5))
    plt.bar(range(256), histogram, width=1, color='black')
    plt.title('Grayscale Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.xlim([0, 255])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
def main():
    # Load a grayscale image
    img = cv.imread('img1.jpg', cv.IMREAD_GRAYSCALE)
    cv.imshow('Grayscale Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    if img is None:
        print("Error: Could not load image.")
        return

    # Calculate histogram
    hist = histogram(img)

    # Plot histogram
    plot_histogram(hist)
    
if __name__ == "__main__":
    main()
# This code calculates and plots the histogram of a grayscale image.
# It initializes a histogram with 256 bins, counts the frequency of each pixel value,
# and then uses matplotlib to visualize the histogram.
# The histogram shows the distribution of pixel intensities in the image.
# Note: Make sure to replace 'image.jpg' with the path to your actual image file.
# The histogram is a graphical representation of the distribution of pixel intensities in an image.