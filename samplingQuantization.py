# SAMPLING AND QUANTIZATION

import cv2 as cv
import numpy as np

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#print(flags)

inputImg = cv.imread("scenery.jpg")

'''
# display the image as such
cv.imshow('Input Image', inputImg)
cv.waitKey(0)
'''

'''
# display the image after converting to gray
grayImg = cv.cvtColor(inputImg, cv.COLOR_RGB2GRAY)
cv.imshow("Gray Image", grayImg)
cv.waitKey(0)
'''

'''
# resize an image
resizeImg = cv.resize(inputImg, (200, 200))
cv.imshow("Resized Image", resizeImg)
cv.waitKey(0)
cv.imwrite("Resized_Image.jpg", resizeImg)
'''

# convert to HSV and extract specific color images
hsv = cv.cvtColor(inputImg, cv.COLOR_BGR2HSV)

# to extract green
green = np.uint8([[[0, 255, 0]]])
hsvGreen = cv.cvtColor(green, cv.COLOR_BGR2HSV)

hueGreen = hsvGreen[0][0][0]
lowerGreen = np.array([hueGreen - 10, 100, 100])
upperGreen = np.array([hueGreen + 10, 255, 255]) 

maskGreen = cv.inRange(hsv, lowerGreen, upperGreen)

# to extract blue
blue = np.uint8([[[255, 0, 0]]])
hsvBlue = cv.cvtColor(blue, cv.COLOR_BGR2HSV)

hueBlue = hsvBlue[0][0][0]
lowerBlue = np.array([hueBlue - 10, 100, 100])
upperBlue = np.array([hueBlue + 10, 255, 255])

maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)

mask = maskGreen + maskBlue

res = cv.bitwise_and(inputImg, inputImg, mask=mask)

cv.imshow("Masked", mask)
cv.waitKey(0)
cv.imshow("Green", res)
cv.waitKey(0)
