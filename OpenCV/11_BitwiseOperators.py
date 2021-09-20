"""In this code we wanna get familiar with\
bitwise operations like bitwise_and(), bitwise_or(),\
bitwise_xor(), and bitwise_not()."""

import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 0, 255), -1)
img2 = cv2.imread("Medias/image_1.png")

###############################################################################
BitAnd = cv2.bitwise_and(img2, img1)
"""
bitwise_and(src1, src2[, dst[, mask]]) -> dst

Parameters:
src1 – first input array or a scalar.

src2 – second input array or a scalar.

src – single input array.

value – scalar value.

dst – output array that has the same size and type as the input arrays.

mask – optional operation mask, 8-bit single channel array,
that specifies elements of the output array to be changed.

For each pixel:
    dst = min{BGR(scr1), BGR(scr2)}
"""

###############################################################################
BitOr = cv2.bitwise_or(img2, img1)
"""
cv2.bitwise_or(src1, src2[, dst[, mask]]) → dst

Parameters:
src1 – first input array or a scalar.

src2 – second input array or a scalar.

src – single input array.

value – scalar value.

dst – output array that has the same size and type as the input arrays.

mask – optional operation mask, 8-bit single channel array,
that specifies elements of the output array to be changed.

For each pixel:
    dst = max{BGR(scr1), BGR(scr2)}
"""

###############################################################################
BitXor = cv2.bitwise_xor(img2, img1)
"""
cv2.bitwise_xor(src1, src2[, dst[, mask]]) → dst

Parameters:
src1 – first input array or a scalar.

src2 – second input array or a scalar.

src – single input array.

value – scalar value.

dst – output array that has the same size and type as the input arrays.

mask – optional operation mask, 8-bit single channel array,
that specifies elements of the output array to be changed.

For each pixel:
    dst = max{BGR(scr1), BGR(scr2)} - min{BGR(scr1), BGR(scr2)}
"""

###############################################################################
BitNot1 = cv2.bitwise_not(img1)
BitNot2 = cv2.bitwise_not(img2)

"""
cv2.bitwise_not(src[, dst[, mask]]) → dst

Parameters:
src – input array.
dst – output array that has the same size and type as the input array.
mask – optional operation mask, 8-bit single channel array,
that specifies elements of the output array to be changed.

For each pixel:
    dst = (255, 255, 255) - BGR(scr)
"""

###############################################################################


cv2.imshow('image1', img1)
cv2.imshow('image2', img2)

cv2.imshow('BitAnd', BitAnd)
cv2.imshow('BitOr', BitOr)
cv2.imshow('BitXor', BitXor)
cv2.imshow('BitNot1', BitNot1)
cv2.imshow('BitNot2', BitNot2)


cv2.waitKey(0)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('q'):
    cv2.destroyAllWindows()
