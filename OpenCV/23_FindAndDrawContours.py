"""
Let's get familiar with contours.

Contours can be explained simply as a curve joining all the continuous points
(along the boundary), having same color or intensity. The contours are
a useful tool for shape analysis and object detection and recognition.
"""
import cv2
# import numpy as np

img = cv2.imread("Medias/opencv-logo2.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 127, 255, 0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
"""
findContours(image, mode, method[, contours[, hierarchy[, offset]]])
-> contours, hierarchy
"""

print("Number of Contours = " + str(len(contours)))
print(contours[0])
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
"""
drawContours(image, contours, contourIdx, color[, thickness[, lineType
[, hierarchy[, maxLevel[, offset]]]]]) -> image

Pass -1 to third argument to draw all contours.
"""

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
