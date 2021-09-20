"""In this code we wanna replace the background of our video\
with a black screen."""
# import numpy as np
import cv2 as cv


kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
cap = cv.VideoCapture("Medias/vtest.avi")
# cap = cv.VideoCapture(0)


"""
createBackgroundSubtractorMOG2([, history[, varThreshold[, detectShadows]]])
-> retval
bgsm = Background Segment
"""
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv.createBackgroundSubtractorMOG2(detectShadows=True)


"""
createBackgroundSubtractorGMG([, initializationFrames[, decisionThreshold]])
-> retval

This method needs kernel and cv.morphologyEx method to apply properly.
"""
# fgbg = cv.bgsegm.createBackgroundSubtractorGMG()


"""
createBackgroundSubtractorKNN([, history[, dist2Threshold
[, detectShadows]]]) -> retval
"""
# fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True)


while cap.isOpened():

    ret, frame = cap.read()
    if frame is None:
        break
    fgMask = fgbg.apply(frame)

    """morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType
    [, borderValue]]]]]) -> dst """
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel)
    cv.imshow("Frame", frame)
    cv.imshow("FG Mask Frame", fgMask)

    k = cv.waitKey(30) & 0xFF
    if k == 27 or k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
