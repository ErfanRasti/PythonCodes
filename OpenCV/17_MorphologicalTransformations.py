"""In this code we wanna get familiar with morphological transformations."""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Medias/j.png', cv2.IMREAD_GRAYSCALE)
"""We can use 0 instead of cv2.IMREAD_GRAYSCALE ."""

# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
mask = img

kernel = np.ones((5, 5), np.uint8)
"""
ones(shape, dtype=None, order='C')

Description:
Return a new array of given shape and type, filled with ones.

Parameters
shape : int or sequence of ints Shape of the new array, e.g., (2, 3) or 2.
dtype : data-type, optional The desired data-type for the array, e.g.,
numpy.int8. Default is numpy.float64.
order : {'C', 'F'}, optional, default: C Whether to store multi-dimensional
data in row-major (C-style) or column-major (Fortran-style) order in memory.
"""

dilation = cv2.dilate(mask, kernel, iterations=2)
"""
cv2.dilate(src, kernel[, dst[, anchor[, iterations[, borderType
[, borderValue]]]]]) → dst

Parameters:
src – input image; the number of channels can be arbitrary,
but the depth should be one of CV_8U, CV_16U, CV_16S, CV_32F` or ``CV_64F.

dst – output image of the same size and type as src.

element – structuring element used for dilation; if element=Mat() ,
a 3 x 3 rectangular structuring element is used.

anchor – position of the anchor within the element; default value (-1, -1)
means that the anchor is at the element center.

iterations – number of times dilation is applied.

borderType – pixel extrapolation method.

borderValue – border value in case of a constant border.
"""

erosion = cv2.erode(mask, kernel, iterations=1)
"""
  cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType
  [, borderValue]]]]]) → dst
"""

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
mth = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
"""
cv2.morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType
[, borderValue]]]]]) → dst

Opening is another form of erosion followed by dilation.
So when you performe opening, first of all erosion is performed on the image
and then the dilation will be performed  on the image.

closing is another form of dilation followed by erosion.
So when you performe opening, first of all dilation is performed on the image
and then the erosion will be performed  on the image.
"""

titles = ['Image', 'Masked Image', 'Dilatory Form',
          'Erosional Form', 'Opening Form', 'Closing Form',
          'Morphological Gradient', 'Morphological TopHat']

images = [img, mask, dilation, erosion, opening, closing, mg, mth]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
