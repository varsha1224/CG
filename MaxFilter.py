# MAX FILTER

import cv2
import numpy as np

def max_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(image, kernel)

# Example usage
image = cv2.imread("img.png")
kernel_size = 5  # Adjust kernel size as needed
max_filtered_image = max_filter(image, kernel_size)
cv2.imshow("Max Filtered Image", max_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
