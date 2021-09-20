"""Let's detect corners using Shi-Tomasi method.\
We can control the number of corners we want to detect, using this method."""
import numpy as np
import cv2 as cv

img = cv.imread("Medias/pic1.png")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""
goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners
[, mask[, blockSize[, useHarrisDetector[, k]]]]]) -> corners .
"""
corners = cv.goodFeaturesToTrack(grayImg, 100, 0.01, 10)
"""
cv.int0: 64-bit integer. Character code 'l'. Python int compatible.
(We can use cv.int64 instead.)
"""
corners = np.int0(corners)
# corners = np.int64(corners)


for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, (0, 0, 255), -1)

cv.imshow("dst", img)
cv.waitKey()
