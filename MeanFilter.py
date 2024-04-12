# MEAN FILTER

import cv2

def mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

# Example usage
image = cv2.imread("img.png")
kernel_size = 5  # Adjust kernel size as needed
mean_filtered_image = mean_filter(image, kernel_size)
cv2.imshow("Mean Filtered Image", mean_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
