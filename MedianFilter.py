# MEDIAN FILTER

import cv2

def median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)

# Example usage
image = cv2.imread("img.png")
kernel_size = 5  # Adjust kernel size as needed
median_filtered_image = median_filter(image, kernel_size)
cv2.imshow("Median Filtered Image", median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
