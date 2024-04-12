# LOG TRANSFORMATION

import cv2
import numpy as np

def log_transformation(image):
    # Normalizing the pixel values
    normalized_image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # Applying log transformation
    transformed_image = np.log1p(normalized_image)
    # Denormalizing the pixel values
    transformed_image = cv2.normalize(transformed_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return transformed_image

# Example usage
image = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)
log_transformed_image = log_transformation(image)
cv2.imshow("Log Transformed Image", log_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
