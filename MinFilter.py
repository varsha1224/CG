# MIN FILTER

import cv2
import numpy as np

def min_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(image, kernel)

# Example usage
image = cv2.imread("img.png")
kernel_size = 5  # Adjust kernel size as needed
min_filtered_image = min_filter(image, kernel_size)
cv2.imshow("Min Filtered Image", min_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
