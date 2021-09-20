"""In this code we wanna track a car object."""
import numpy as np
import cv2 as cv
cap = cv.VideoCapture("Medias/slow_traffic_small.mp4")

"""Take first frame of the video."""
ret, frame = cap.read()

"""Setup initial location of the window."""
x, y, w, h = 300, 200, 100, 50
trackWindow = (x, y, w, h)

"""Setup the ROI for tracking."""
roi = frame[y:y+h, x:x+w]
hsvROI = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsvROI, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
roiHist = cv.calcHist([hsvROI], [0], mask, [180], [0, 180])
# print(roiHist)
"""
normalize(src, dst[, alpha[, beta[, norm_type[, dtype[, mask]]]]]) -> dst .
@brief Normalizes the norm or value range of an array. . . The function
cv::normalize normalizes scale and shift the input array elements so that .

Parameters:
src – input array.
dst – output array of the same size as src .
alpha – norm value to normalize to or the lower range boundary
in case of the range normalization.
beta – upper range boundary in case of the range normalization;
it is not used for the norm normalization.
normType – normalization type (see the details below).
dtype – when negative, the output array has the same type as src; otherwise,
it has the same number of channels as src and the depth =CV_MAT_DEPTH(dtype).
mask – optional operation mask.
"""
cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)

"""Setup the termination criteria, either 10 iteration or move by
at least 1 pt."""
termCriteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

cv.imshow("RegionOfInterest", roi)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        """calcBackProject(images, channels, hist, ranges, scale[, dst])
        -> dst ."""
        dst = cv.calcBackProject([hsv], [0], roiHist, [0, 180], 1)

        """Apply meanshift to get the new location."""
        # ret, trackWindow = cv.meanShift(dst, trackWindow, termCriteria)
        ret, trackWindow = cv.CamShift(dst, trackWindow, termCriteria)
        print(ret)

        """Draw it on the frame."""
        """boxPoints(box[, points]) -> points . @brief Finds the four vertices
        of a rotated rect. Useful to draw the rotated rectangle. . ."""
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        finalImage = cv.polylines(frame, [pts], True, (0, 0, 255), 2)
        # x, y, w, h = trackWindow
        # finalImage = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 3)

        cv.imshow("dst", dst)
        cv.imshow("Final Image", finalImage)
        keyboard = cv.waitKey(30) & 0xFF
        if keyboard == 27:
            break
    else:
        break
