"""In this code we are gonna get familiar\
with some basic operations on images."""
# import numpy as np
import cv2

img = cv2.imread('Medias/messi5.jpg')
img2 = cv2.imread('Medias/opencv-logo2.png')

############################################################################

print(img.shape)
"""
img.shape returns a tuple of numbers of rows, columns and channels.
channels' Example: RGB image has three channels.
(1. Red
2. Green
3. Blue)
"""

print(img.size)
"""img.size returns the total size of pixels is accessed."""

print(img.dtype)
"""img.dtype returns mage datatype is obtained."""

b, g, r = cv2.split(img)
"""
This line saves the BGR of the pixels in 3 separate variables.

This lineoutputs vector of arrays;
the arrays themselves are reallocated, if needed."""

img = cv2.merge((b, g, r))
"""
cv2.merge(mv, dst=None)

This line merges three variables b,g,r.
(In this case it results the main image.)

The number of channels will be\
the total number of channels in the matrix array.
"""
############################################################################

ball = img[280:340, 330:390]
"""This is the region of the ball."""

img[273:333, 100:160] = ball
"""
This line pastes ball on the determined location.
(This location gives us natural image without cut line sign.
(ROI: Region Of Interest))
"""

############################################################################
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
"""
cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) → dst

Parameters:
src –
input image.

dst –
output image; it has the size dsize (when it is non-zero) or
the size computed from src.size(), fx, and fy;
the type of dst is the same as of src.

dsize –
output image size; if it equals zero, it is computed as:
    dsize = Size(round(fx*src.cols), round(fy*src.rows))

Either dsize or both fx and fy must be non-zero.

fx –
scale factor along the horizontal axis; when it equals 0, it is computed as

    (double)dsize.width/src.cols

fy –
scale factor along the vertical axis; when it equals 0, it is computed as

    (double)dsize.height/src.rows

interpolation –
interpolation method:

INTER_NEAREST - a nearest-neighbor interpolation
INTER_LINEAR - a bilinear interpolation (used by default)
INTER_AREA - resampling using pixel area relation.
It may be a preferred method for image decimation,
as it gives moire’-free results. But when the image is zoomed,
it is similar to the INTER_NEAREST method.
INTER_CUBIC - a bicubic interpolation over 4x4 pixel neighborhood
INTER_LANCZOS4 - a Lanczos interpolation over 8x8 pixel neighborhood

"""


dst = cv2.add(img, img2)
"""
cv2.add(src1, src2[, dst[, mask[, dtype]]]) → dst

Parameters:
src1 – first input array or a scalar.
src2 – second input array or a scalar.
src – single input array.
value – scalar value.
dst – output array that has the same size and type as input arrays.


cv2.add calculates the per-element sum of two arrays or an array and a scalar.
For adding two images, the sizes of two images should be the same.
"""

dst = cv2.addWeighted(img, .5, img2, .5, -110)
"""
cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) → dst


Parameters:
src1 – first input array.
alpha – weight of the first array elements.
src2 – second input array of the same size and channel number as src1.
beta – weight of the second array elements.
dst – output array that has the same size and number of channels
as the input arrays.
gamma – scalar added to each sum.
dtype – optional depth of the output array;
when both input arrays have the same depth,
dtype can be set to -1, which will be equivalent to src1.depth().


The function can be replaced with a matrix expression:
dst = src1*alpha + src2*beta + gamma;

(if gamma>0 then brightness will be increased and
if gamma<0 then brightness will be decreased.)
"""

############################################################################


cv2.imshow('image', dst)
cv2.waitKey(0)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('img_copy.jpg', dst)
    cv2.destroyAllWindows()
