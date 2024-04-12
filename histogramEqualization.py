# HISTOGRAM EQUALIZATION

import cv2
import numpy as np
import random   
import matplotlib.pyplot as plt

image = cv2.imread('b_w.jpg', cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist(image, [0], None, [256], [0, 256])

plt.xlabel("pixel value")
plt.ylabel("count")
plt.plot(histogram)
plt.legend()
plt.show()

eq_histogram_image = cv2.equalizeHist(image)
eq_histogram = cv2.calcHist(eq_histogram_image, [0], None, [256], [0, 256])


plt.xlabel("pixel value")
plt.ylabel("count")
plt.plot(eq_histogram)
plt.legend()
plt.show()

cv2.imshow("original", image)
cv2.waitKey(0)

cv2.imshow("Equalized", eq_histogram_image)
cv2.waitKey(0)

cv2.destroyAllWindows()