"""In this code we wanna get familiar with histograms."""
import cv2
# import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("Medias/lena.jpg")
# img = np.zeros((200,200), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
b, g, r = cv2.split(img1)

cv2.imshow("img", img1)
cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

#####################################################################
"""
hist(x, bins=None, range=None, density=False, weights=None,
cumulative=False, bottom=None, histtype='bar', align='mid',
orientation='vertical', rwidth=None, log=False, color=None,
label=None, stacked=False, *, data=None, **kwargs)

bins:
number of rectangles

range:
range of columns on x-axis
"""

plt.hist(b.ravel(), bins=256, range=[0, 256])
plt.hist(g.ravel(), bins=256, range=[0, 256])
plt.hist(r.ravel(), bins=256, range=[0, 256])


#####################################################################
img2 = cv2.imread("Medias/lena.jpg", 0)
plt.hist(img2.ravel(), bins=256, range=[0, 256])
hist = cv2.calcHist([img2], [0], None, [256], [0, 256])
"""calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
-> hist"""
plt.plot(hist)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
