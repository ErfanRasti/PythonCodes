"""
In this code we wanna get familiar with image pyramids.

In image pyramid, the resolution of upper image is lower than the resolution\
of previous image. The base of the pyramid is the original image.

There are two types of image pyramids:
1. Gaussian Pyramids
2. Laplacian Pyramids

Appplications:
These image pyramids help us to blend and reconstruct the images.
Normally, we used to work with an image of constant size.But in
some occasions, we need to work with images of different resolution
of the same image. For example, while searching for something in an image,
like face, we are not sure at what size the object will be present in the
image. In that case, we will need to create a set of images with different
resolution and search for object in all the images.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Medias/lena.jpg")
layer = img.copy()


"""
Methods:
cv2.pyrDown(src[, dst[, dstsize[, borderType]]]) → dst
cv2.pyrUp(src[, dst[, dstsize[, borderType]]]) → dst
"""

########################################################################

"""Gaussian Pyramid"""
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)
# cv2.imshow("Original Image", img)

########################################################################
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# hr1 = cv2.pyrUp(lr2)
# cv2.imshow('lr1', lr1)
# cv2.imshow('lr2', lr2)
# cv2.imshow('hr1', hr1)
"""
When we use pyrDown method, we lose the information about the image.
So when we pyrUp the lr2 the image is little bit blurred\
because some of the information is loosed using the pyrDown method.
"""
########################################################################
"""Laplacian Pyramid"""
"""
A level in Laplacian Pyramid is formed by difference between\
that level in Gaussian Pyramid and expended version of\
its upper level in Gaussian Pyramid.
"""
layer = gp[-1]
cv2.imshow("Upper Level Gaussian Pyramid", layer)
lp = [layer]

for i in range(6, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    """
    subtract(src1, src2[, dst[, mask[, dtype]]]) -> dst

    Difference between two arrays, when both input arrays have\
    the same size and the same number of .
    """

    lp.append(layer)
    cv2.imshow(str(i), laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()
