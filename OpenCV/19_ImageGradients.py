"""In this code we wanna get familiar with gradient edge detection."""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Medias/sudoku.png", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
"""
cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])
→ dst
"""
lap = np.uint8(np.absolute(lap))
"""Output datatype is cv2.CV_8U or np.uint8. But there is
a slight problem with that. Black-to-White transition is taken as
Positive slope (it has a positive value) while White-to-Black transition
is taken as a Negative slope(It has negative value). So when you convert data
to np.uint8, all negative slopes are made zero. In simple words, you
miss that edge.
If you want to detect both edges, better option is to keep the output datatype
to some higher forms, like cv2.CV_16S, cv2.CV_64F etc, take its absolute value
and then convert back to cv2.CV_8U.
"""

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
"""
Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])
-> dst
"""
sobelCombined = cv2.bitwise_or(sobelX, sobelY)


titles = ['Image', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel Combined']
images = [img, lap, sobelX, sobelY, sobelCombined]


for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
