"""
Let's get familiar with hough transform.

Hough Transform is a popular technique to detect any shape,
if you can represent that shape in mathematical form. It can
detect the shape even if it is broken or distorted a little bit.

Hough Transform Algorithm:
1. Edge detection, e.g. using the Canny edge detector.
2. Mapping of edge points to the Hough space and storage\
    in an accumulator.
3. Interpretation of accumulator to yield lines of infinite length.
The interpretation is done by thresholding and possibly other constraints.
4. Conversion of infinite lines to finite lines.

OpenCV implements two kind of Hough Line Transform:
1. The Standard Hough Line Transform (HoughLines Method)
2. The Probabilistic Hough Line Transform (HoughLinesP method)
"""
import cv2
import numpy as np

img = cv2.imread("Medias/sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=200)
"""
HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta
[, max_theta]]]]])-> lines .
@brief Finds lines in a binary image using the standard Hough transform. . .
The function implements the standard or standard multi-scale Hough transform
algorithm for line .
"""

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    """We wanna find two points on the line to draw that."""
    x0 = rho*a
    y0 = rho*b

    x1 = int(x0-(1000*y0))
    y1 = int(y0+(1000*x0))

    x2 = int(x0+(1000*y0))
    y2 = int(y0-(1000*x0))
    """
    (x0, y0), (x1, y1), (x2, y2) all three are on the line
    rho=x * cos(theta) + y * sin(theta) .
    But we choose (x1, y1) and (x2, y2) because they're two far from eachother
    and they look like infinite line.
    """
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
We can see we doesn't get good result from The Standard Hough Line
Transform. In the next code we're gonna see how to do it using
The Probabilistic Hough Line Transform.
"""
