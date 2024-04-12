# HISTOGRAM MATCHING

import cv2
import numpy as np

def histogram_matching(source, reference):
    # Calculate the histograms.
    src_hist, bins = np.histogram(source.flatten(), 256, [0,256])
    ref_hist, bins = np.histogram(reference.flatten(), 256, [0,256])

    # Calculate the cumulative distribution function for both histograms.
    src_cdf = np.cumsum(src_hist)
    src_cdf_normalized = src_cdf / float(src_cdf.max())
    ref_cdf = np.cumsum(ref_hist)
    ref_cdf_normalized = ref_cdf / float(ref_cdf.max())

    # Create a lookup table to map pixel values from the source to the reference.
    lookup_table = np.zeros(256)
    g_j = 0
    for g_i in range(256):
        while ref_cdf_normalized[g_j] < src_cdf_normalized[g_i] and g_j < 255:
            g_j += 1
        lookup_table[g_i] = g_j

    # Map the pixel values of the source image through the lookup table.
    matched_image = lookup_table[source.flatten()].reshape(source.shape).astype(np.uint8)

    return matched_image

# Load source and reference images
source_img = cv2.imread('scenery.jpg', cv2.IMREAD_GRAYSCALE)
reference_img = cv2.imread('b_w.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram matching
matched_img = histogram_matching(source_img, reference_img)

# Display the result
cv2.imshow('Source Image', source_img)
cv2.imshow('Reference Image', reference_img)
cv2.imshow('Matched Image', matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
