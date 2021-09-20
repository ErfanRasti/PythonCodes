"""In this code we wanna change a number of a photo via trackbar."""
# import numpy as np
import cv2 as cv


def nothing(x):
    """Print the Changing value."""
    print(x)


cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv.imread('Medias/lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 1, (0, 0, 255), 4)
    """This line puts a number on the photo."""

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
        break
    elif k == ord('s'):
        dst = 0
        cv.imwrite('img_copy.jpg', dst)
        cv.destroyAllWindows()
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    """
    If the switch trackbar is setted on 0 the original photo will be shown
    and if the switch trackbar is setted on 1 the screen color will
    be changed to gray form.
    """

    cv.imshow('image', img)
