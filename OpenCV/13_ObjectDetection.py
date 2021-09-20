"""
In this code we wanna detect an object via OpenCV.

HSV(Hue, Situration, Value)

Hue, corresponds to the color components (base pigment),
hence just by selecting a range of Hue you can select any color.
(0 - 360)

Saturation, is the amount of color (depth of the pigment)
(dominance of Hue) (0 - 100%)

Value is basically the brightness of the color. (0 - 100%)

(For HSV, hue range is [0,179], saturation range is [0,255],
and value range is [0,255]. Different software use different scales.
So if you are comparing OpenCV values with them,
you need to normalize these ranges.)
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
"""Review 2_Capturing&SavingVideo.py ."""


def nothing(x):
    """
    Pass nothing.

    This function does nothing. It's just for passing
    as fourth argument of cv.createTrackbar.
    """
    pass


Trackbars = np.zeros((100, 512, 3), np.uint8)
"""This image is for showing the average color of the range."""
cv2.namedWindow("Tracking")

"""Defineing the range of Hue"""
cv2.createTrackbar("LH", "Tracking", 0, 180, nothing)
cv2.createTrackbar("UH", "Tracking", 180, 180, nothing)
"""Defineing the range of Saturation"""
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
"""Defineing the range of Value"""
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    # frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """
    This hsv variable is an array that contains
    hsv color code of our image.
    (It's not appropriate for showing.)
    """
    """Getting the trackbar position for setting the range of mask"""
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    """Getting the average of the hsv range"""
    mh = (l_h+u_h)/2
    ms = (l_s+u_s)/2
    mv = (l_v+u_v)/2
    """converting HSV color space to BGR color space"""
    hsv_color = np.uint8([[[mh, ms, mv]]])
    bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)
    Trackbars[:] = bgr_color

    l_c = np.array([l_h, l_s, l_v])
    u_c = np.array([u_h, u_s, u_v])
    """These arrays are in HSV color space."""

    mask = cv2.inRange(hsv, l_c, u_c)
    """
    cv2.inRange(src, lowerb, upperb[, dst]) → dst

    Parameters:
    src – first input array.
    lowerb – inclusive lower boundary array or a scalar.
    upperb – inclusive upper boundary array or a scalar.
    dst – output array of the same size as src and CV_8U type.

    This function limits the frame on the defined range.
    """
    res = cv2.bitwise_and(frame, frame, mask=mask)
    """
    The first and second arguments of cv2.bitwise_and are the same,
    but as the third argument we filter the output via mask array.
    """
    cv2.imshow("Tracking", Trackbars)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
