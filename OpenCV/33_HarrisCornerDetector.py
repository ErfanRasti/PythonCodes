"""In this code we wanna detect corners using Harriscorner method."""

import numpy as np
import cv2 as cv

img = cv.imread("Medias/chessboard.png")
img = cv.resize(img, (300, 300))
cv.imshow("Original Image", img)
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""cv.cornerHarris method takes grayscale image in float32."""
grayImg = np.float32(grayImg)

"""
cornerHarris(src, blockSize, ksize, k[, dst[, borderType]]) -> dst .

img - Input image. It should be grayscale and float32 type.
blockSize - It is the size of neighborhood considered for corner detection
ksize - Aperture parameter of the Sobel derivative used.
k - Harris detector free parameter in the equation.
"""
dst = cv.cornerHarris(grayImg, 2, 3, 0.04)
"""result is dilated for marking the corners, not important."""
dst = cv.dilate(dst, None)
"""Threshold for an optimal value, it may vary depending on the image."""
img[dst > 0.01*dst.max()] = [0, 0, 255]
cv.imshow("dst", img)
cv.waitKey()
