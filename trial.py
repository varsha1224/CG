import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sudoku.jpg", cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)

plt.subplot(2, 2, 1), plt.imshow(img, cmap="gray")
plt.title("Original")

plt.subplot(2, 2, 2), plt.imshow(lap, cmap="gray")
plt.title("laplacian")

plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap="gray")
plt.title("Sobel x")

plt.subplot(2, 2, 4), plt.imshow(sobely, cmap="gray")
plt.title("Sobel y")
