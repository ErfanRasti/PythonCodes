"""This code shows the color of the position\
where we clicked left button down."""
import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
"""These lines of code list out all of the events in cv2 package."""


def click_events(event, x, y, flags, param):
    """
    Show the color of the position where we clicked left button down,\
    in a new window.

    Args:
        event ([int]): What kind of click is it?
        x ([int]): The x coordinate of the postion where event occurred.
        y ([int]): The y coordinate of the postion where event occurred.
        flags ([type]): [description] (IDK)
        param ([type]): [description] (IDK)
    """
    if event is cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        red = img[x, y, 1]
        green = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        MyColorImage = np.zeros((512, 512, 3), np.uint8)
        MyColorImage[:] = [blue, red, green]
        """
        This line colors whole of the np.zeros image\
        with the BGR of the position where we clicked left button down.
        """
        cv2.imshow('color', MyColorImage)


img = cv2.imread('Medias/lena.jpg')
# img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
points = list()

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
