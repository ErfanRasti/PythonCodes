"""
In this code we wanna adapt our thresholding.

Adaptive thresholding is the method where the trashold value is calculated
for the smaller region; So the threshold is not global for every pixel.
but it calculated for smaller region and therefore there will be different
thrashold value for different regions.
"""
import cv2
import matplotlib.pyplot as plt
# import numpy as np


img = cv2.imread('Medias/sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
"""
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType,
                        blockSize, C[, dst]) → dst

Parameters:
src – Source 8-bit single-channel image.

dst – Destination image of the same size and the same type as src .

maxValue – Non-zero value assigned to the pixels for which the condition
is satisfied. See the details below.

adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C
or ADAPTIVE_THRESH_GAUSSIAN_C . See the details below.

thresholdType – Thresholding type that must be either THRESH_BINARY
or THRESH_BINARY_INV .

blockSize – Size of a pixel neighborhood that is used to calculate
a threshold value for the pixel: 3, 5, 7, and so on.

C – Constant subtracted from the mean or weighted mean (see the details below).
Normally, it is positive but may be zero or negative as well.





- For the method ADAPTIVE_THRESH_MEAN_C , the threshold value T(x,y)
is a mean of the blockSize * blockSize neighborhood of (x, y) minus C.

- For the method ADAPTIVE_THRESH_GAUSSIAN_C , the threshold value T(x, y)
is a weighted sum (cross-correlation with a Gaussian window)
of the blockSize * blockSize neighborhood of (x, y) minus C .
The default sigma (standard deviation) is used for the specified blockSize.




- THRESH_BINARY:
(It's binary.(0 or 1))
    if src(x, y) > T(x, y):
        dst(x, y) = maxval
    else:
        dst(x,y) = 0
- THRESH_BINARY_INV
INV(abbreviation of inverted)
    if src(x, y) > T(x, y):
        dst(x,y) = 0
"""
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 4)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


# cv2.imshow('image', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)


titles = ['Original Image', 'Simple Thresholding',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding ']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()


# k = cv2.waitKey(0) & 0xFF
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('img_copy.jpg', img)
#     cv2.destroyAllWindows()
