"""In this code we wanna adjust the color of the screen via trackbars."""
import cv2
import numpy as np
from numpy.lib.shape_base import dstack


def nothing(x):
    """Print the Changing value."""
    print(x)


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
"""
namedWindow(winname[, flags]) -> None

Parameters:
name – Name of the window in the window caption that
may be used as a window identifier.

flags – Flags of the window. The supported flags are:

- WINDOW_NORMAL If this is set, the user can resize the window (no constraint).
- WINDOW_AUTOSIZE If this is set, the window size is automatically
adjusted to fit the displayed image (see imshow() ),
and you cannot change the window size manually.
- WINDOW_OPENGL If this is set, the window will be created with OpenGL support.
"""

###############################################################################
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF and 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

"""
cv.CreateTrackbar(trackbarName, windowName, value, count, onChange) → None

Parameters:
trackbarname – Name of the created trackbar.

winname – Name of the window that will be used
as a parent of the created trackbar.

value – Optional pointer to an integer variable whose value reflects
the position of the slider. Upon creation, the slider position
is defined by this variable.

count – Maximal position of the slider. The minimal position is always 0.

onChange – Pointer to the function to be called every time the slider
changes position. This function should be prototyped as void Foo(int,void*);
, where the first parameter is the trackbar position and the second parameter
is the user data (see the next parameter). If the callback is the NULL pointer,
no callbacks are called, but only value is updated.

userdata – User data that is passed as is to the callback. It can be used to
handle trackbar events without using global variables.
"""
###############################################################################

while (1):

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):
        cv2.imwrite('img_copy.jpg', dstack)
        cv2.destroyAllWindows()
        break
###############################################################################
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    """
    cv2.getTrackbarPos(trackbarname, winname) → retval

    Parameters:
    trackbarname – Name of the trackbar.

    winname – Name of the window that is the parent of the trackbar.


    The function returns the current position of the specified trackbar.
    """

    if s == 0:
        img[:] = 0
        """ This line set the color of the screen to black."""

    else:
        img[:] = [b, g, r]
        """ This line adjusts the color of
        the screen according to trackbars."""

    """
    If the switch trackbar is setted on 0 the screen color won't be changed
    and if the switch trackbar is setted on 1 the screen color will be changed.
    """

    cv2.imshow('image', img)
    """
    The first argument of cv2.imshow is is equal with trackbars' name.
    So img and trackbars will be shown in one image together.
    """

###############################################################################
    # End of while
