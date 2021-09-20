"""In this code we wanna use matplotlib with opencv."""
import cv2
# import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Medias/lena.jpg', -1)
cv2.imshow('image', img)
"""
OpenCV reads images in BGR format, but
Matplotlib reads images in RGB format.

So we need to convert our image form BGR to RBG.
"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""
matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None,
interpolation=None,alpha=None, vmin=None, vmax=None, origin=None,
extent=None, shape=<deprecated parameter>, filternorm=1, filterrad=4.0,
imlim=<deprecated parameter>, resample=None, url=None, *, data=None, **kwargs)

X : array-like or PIL image
The image data. Supported array shapes are:

(M, N): an image with scalar data. The data is visualized using a colormap.
(M, N, 3): an image with RGB values (0-1 float or 0-255 int).
(M, N, 4): an image with RGBA values (0-1 float or 0-255 int),
i.e. including transparency.
The first two dimensions (M, N) define the rows and columns of the image.

Out-of-range RGB(A) values are clipped.

For more details see:
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
"""
plt.imshow(img)

plt.xticks([]), plt.yticks([])
""" This line hides the x, y axises."""

plt.show()

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('img_copy.jpg', img)
    cv2.destroyAllWindows()
