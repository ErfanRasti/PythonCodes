"""
In this code we wanna blur images with various low pass filters\
and apply custom-made filters to images (2D convolution).

In image proccessing, a kernel, convolution matrix,
or mask is a small matrix. It is used for blurring,
sharpening, embossing, edge detection, and more.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('opencv-logo2.png')
# img = cv2.imread('HalftoneGaussianBlur.jpg')
# img = cv2.imread('SaltAndPepperNoise.png')
img = cv2.imread('Medias/lena.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
"""
Kernel = (1/(K(width).K(height)))(np.ones(K(height), K(width)))
"""

dst = cv2.filter2D(img, -1, kernel)
"""
filter2D(src, ddepth, kernel, dst=None, anchor=None,
delta=None, borderType=None)

As for one-dimensional signals, images also can be filtered with
various low-pass filters (LPF), high-pass filters (HPF), etc.
A LPF helps in removing noise, or blurring the image.
A HPF filters helps in finding edges in an image.
"""

blur = cv2.blur(img, (5, 5))
"""cv2.blur(src, ksize[, dst[, anchor[, borderType]]]) → dst"""

gbl = cv2.GaussianBlur(img, (5, 5), 0)
"""
cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) → dst

Parameters:
src – input image; the image can have any number of channels,
which are processed independently, but the depth should be CV_8U, CV_16U,
CV_16S, CV_32F or CV_64F.

dst – output image of the same size and type as src.

ksize – Gaussian kernel size. ksize.width and ksize.height can differ
but they both must be positive and odd. Or, they can be zero’s and then
they are computed from sigma* .

sigmaX – Gaussian kernel standard deviation in X direction.

sigmaY – Gaussian kernel standard deviation in Y direction; if sigmaY is zero,
it is set to be equal to sigmaX, if both sigmas are zeros, they are computed
from ksize.width and ksize.height , respectively (see getGaussianKernel()
for details); to fully control the result regardless of possible future
modifications of all this semantics, it is recommended to specify all of ksize,
sigmaX, and sigmaY.

borderType – pixel extrapolation method (see borderInterpolate() for details).
"""

median = cv2.medianBlur(img, 5)
"""
cv2.medianBlur(src, ksize[, dst]) → dst

The function cv2.medianBlur() computes the median of all the pixels
under the kernel window and the central pixel is replaced
with this median value. This is highly effective in removing
salt-and-pepper noise.
"""

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
"""
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]])
→ dst
"""


titles = ['image', '2D Convolution',
          'Blur Image', 'Gaussian Blur', 'Median Blur', 'Bilateral Blur']
images = [img, dst, blur, gbl, median, bilateral]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
