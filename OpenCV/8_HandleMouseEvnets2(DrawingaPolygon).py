"""In this code we wanna draw a polygon via mouse events."""
import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
"""These lines of code list out all of the events in cv2 package."""


def click_events(event, x, y, flags, param):
    """
    Draw a line with clicking left button down\
    on two coordinates.

    Args:
        event ([int]): What kind of click is it?
        x ([int]): The x coordinate of the postion where event occurred.
        y ([int]): The y coordinate of the postion where event occurred.
        flags ([type]): [description] (IDK)
        param ([type]): [description] (IDK)
    """
    if event is cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 4)
        cv2.imshow('image', img)


# img = cv2.imread('lena.jpg')
img = np.zeros((512, 512, 3), np.uint8)
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
