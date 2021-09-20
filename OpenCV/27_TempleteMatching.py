"""In this code we wanna match a template in a image."""
import cv2
import numpy as np
# import matplotlib.pyplot as plt
img = cv2.imread("Medias/messi5.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Medias/messi_face.jpg", 0)
h, w = template.shape
# w, h = template.shape[::-1]
"""
img.shape returns (Height, Width, Channel).
But in this case we have a grayscale image;
So it returns (Height, Width).
"""


# res = cv2.matchTemplate(image=grayImg, templ=template,
#                         method=cv2.TM_CCOEFF_NORMED)
res = cv2.matchTemplate(image=grayImg, templ=template,
                        method=cv2.TM_CCORR_NORMED)
"""
matchTemplate(image, templ, method[, result[, mask]]) -> result .
@brief Compares a template against overlapped image regions. . .
The function slides through image , compares the overlapped patches of size
\f$w \times h\f$ against .
"""
print(res)
threshold = 0.99
loc = np.where(res >= threshold)
"""where(condition, x=None, y=None) -> tuple"""
print(loc)
for pt in zip(*loc[::-1]):
    """zip(*iterables) --> zip object"""
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
