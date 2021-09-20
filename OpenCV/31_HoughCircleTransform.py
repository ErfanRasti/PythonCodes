"""Let's find the circles using HoughCircles."""
import cv2
import numpy as np
img = cv2.imread("Medias/Shapes1.jpg")
output = img.copy()
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImg = cv2.medianBlur(grayImg, 5)
circles = cv2.HoughCircles(grayImg,
                           cv2.HOUGH_GRADIENT,
                           1, 20, param1=50,
                           param2=40,
                           minRadius=0,
                           maxRadius=0)
# This line makes an array with rounded values of  circles array.
detectedCircles = np.uint16(np.around(circles))
print(circles)
print(detectedCircles)
for (x, y, r) in detectedCircles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 20), thickness=2)
    # It represent a dot.
    cv2.circle(output, (x, y), 1, (0, 255, 255), thickness=2)


cv2.imshow("Smarties", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""around(a, decimals=0, out=None) -> None"""
"""
HoughCircles(image, method, dp, minDist[, circles[, param1[, param2
[, minRadius[, maxRadius]]]]]) -> circles .
@brief Finds circles in a grayscale image using the Hough transform. . .
The function finds circles in a grayscale image using a modification
of the Hough transform. . .


Parameters:
image – 8-bit, single-channel, grayscale input image.

circles – Output vector of found circles. Each vector is encoded
as a 3-element floating-point vector (x, y, radius) .

circle_storage – In C function this is a memory storage that will contain
the output sequence of found circles.

method – Detection method to use. Currently, the only implemented method
is CV_HOUGH_GRADIENT , which is basically 21HT , described in [Yuen90].

dp – Inverse ratio of the accumulator resolution to the image resolution.
For example, if dp=1 , the accumulator has the same resolution
as the input image. If dp=2 , the accumulator has half as big width and height.

minDist – Minimum distance between the centers of the detected circles.
If the parameter is too small, multiple neighbor circles may be falsely
detected in addition to a true one. If it is too large, some circles
may be missed.

param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT ,
it is the higher threshold of the two passed to the Canny() edge detector
(the lower one is twice smaller).

param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT ,
it is the accumulator threshold for the circle centers at the detection stage.
The smaller it is, the more false circles may be detected. Circles,
corresponding to the larger accumulator values, will be returned first.

minRadius – Minimum circle radius.

maxRadius – Maximum circle radius.
"""
