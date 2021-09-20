"""In this code we are trying to set camera parameters."""
import cv2
cap = cv2.VideoCapture(0)

print('Frame Width: ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame Height: ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cv2.CAP_PROP_FRAME_WIDTH == 3
# cv2.CAP_PROP_FRAME_HEIGHT == 4

cap.set(3, 1200)
cap.set(4, 1200)
"""
set(​propId, value​)

propID is a number from 0 to 18:
0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured
next.
2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5. CV_CAP_PROP_FPS Frame rate.
6. CV_CAP_PROP_FOURCC 4-character code of codec.
7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should
be converted to RGB.
17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras
(note: only supported by DC1394 v 2.x backend currently)

if the width and height is more than maximum,
it will automatically set to maximum size.
"""

print('Frame Width: ', cap.get(3))
print('Frame Height: ', cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        effect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', effect)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
