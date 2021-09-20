"""In this code we wanna get familiar with thresholding."""
import cv2
import matplotlib.pyplot as plt
# import numpy as np


img = cv2.imread('Medias/gradient.png', 0)


"""
cv2.threshold(src, thresh, maxval, type[, dst]) -> retval, dst

Two outputs are obtained:
First one is a retval.
Second output is our thresholded image.

Parameters:
src – input array (single-channel, 8-bit or 32-bit floating point).
thresh – threshold value.
maxval – maximum value to use with the THRESH_BINARY\
and THRESH_BINARY_INV thresholding types.
type – thresholding type (see the details below).
dst – output array of the same size and type as src.


There are several types of thresholding supported by the function.
They are determined by type :


    - THRESH_BINARY:
    (It's binary.(0 or 1))
        if src(x, y) > thresh:
            dst(x, y) = maxval
        else:
            dst(x,y) = 0

    - THRESH_BINARY_INV
    INV(abbreviation of inverted)
        if src(x, y) > thresh:
            dst(x,y) = 0
        else:
            dst(x, y) = maxval

    - THRESH_TRUNC
        if src(x, y) > thresh:
            dst(x,y) = threshold
        else:
            dst(x, y) = src(x, y)

    - THRESH_TOZERO
        if src(x, y) > thresh:
            dst(x,y) = src(x, y)
        else:
            dst(x, y) = 0

    - THRESH_TOZERO_INV
        if src(x, y) > thresh:
            dst(x, y) = 0
        else:
            dst(x,y) = src(x, y)

"""

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


# cv2.imshow('Image', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)
# cv2.imshow('th5', th5)

"""A little Matplot"""

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()


# k = cv2.waitKey(0) & 0xFF
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('img_copy.jpg', img)
#     cv2.destroyAllWindows()
