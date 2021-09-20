"""
There are many mouse events available in cv2 package.\
In this code we wanna handle this mouse events.

(Acccessing Coordinate and BGR of a point)
"""
import cv2
# import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
"""These lines of code list out all of the events in cv2 package."""


def click_events(event, x, y, flags, param):
    """
    Show the coordinate of the position where we clicked left button down\
    and show the BGR of the position where we clicked right button down.

    Args:
        event ([int]): What kind of click is it?
        x ([int]): The x coordinate of the postion where event occurred.
        y ([int]): The y coordinate of the postion where event occurred.
        flags ([type]): [description] (IDK)
        param ([type]): [description] (IDK)
    """
    if event is cv2.EVENT_LBUTTONDOWN:
        """
        If you click left button down the coordinate of the postion
        where we clicked left button down, will be shown.
        """
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = f'{x}, {y}'
        cv2.putText(img, strXY, (x, y), font, .3, (255, 0, 0), 1)
        cv2.imshow('image', img)

    if event is cv2.EVENT_RBUTTONDOWN:
        """
        If you click right button down the BGR of the the postion
        where we clicked right button down, will be shown.
        """
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        """
         img Args:
            1. y coordinate
            2. x coordinate
            3. BGR (0 for B 1 for G and 2 for R)
        """
        print(f'{blue}, {green}, {red}')
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = f'{blue}, {red}, {green}'
        cv2.putText(img, strBGR, (x, y), font, .3,
                    (int(255-blue), int(255-green), int(255-red)), 1)
        """These lines of code print out the BGR
        of the of the position where we clicked down
        on the image.
        The color of this text is opposite of the coordinate color.
        """
        cv2.imshow('image', img)


img = cv2.imread('Medias/lena.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
"""
setMouseCallback(windowName, onMouse [, param]) -> None
"""
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('img_copy.jpg', img)
    cv2.destroyAllWindows()
