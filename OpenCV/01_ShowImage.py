"""In this projet we're trying to show an image via python."""
import cv2

img = cv2.imread('Medias/lena.jpg', 1)
"""
Syntax: cv2.imread(path, flag)

Parameters:

path: A string representing the path of the image to be read.

flag: It specifies the way in which image should be read.
It’s default value is cv2.IMREAD_COLOR

Return Value: This method returns an image
that is loaded from the specified file.

////////////////////////////////////////////////////////////////////

The second argument of this function has three values: -1, 0, 1

cv2.IMREAD_COLOR: It specifies to load a color image.
Any transparency of image will be neglected.
It is the default flag. Alternatively,
we can pass integer value 1 for this flag.

cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode.
Alternatively, we can pass integer value 0 for this flag.

cv2.IMREAD_UNCHANGED: It specifies to load an image as
such including alpha channel. Alternatively,
we can pass integer value -1 for this flag.
"""
print(img)

cv2.imshow('image', img)
"""
Syntax: cv2.imshow(window_name, image)

Parameters:

window_name: A string representing the name of
the window in which image to be displayed.

image: It is the image that is to be displayed.

Return Value: It doesn’t returns anything.
"""

k = cv2.waitKey(0)
"""
cv2.waitKey() is a keyboard binding function.
Its argument is the time in milliseconds.
The function waits for specified milliseconds for any keyboard event.
If you press any key in that time, the program continues.
If 0 is passed, it waits indefinitely for a key stroke.
It can also be set to detect specific key strokes like,
if key a is pressed etc which we will discuss below.
"""

if k == 27:
    """Wait for ESC key to exit.
    (ASCII code of ESC is 27.)"""
    cv2.destroyAllWindows()
    """
    cv2.destroyAllWindows() simply destroys all the windows we created.
    If you want to destroy any specific window,
    use the function cv2.destroyWindow()
    where you pass the exact window name as the argument.
    """
elif k == ord('s'):
    """Wait for 's' key to save and exit.
    (ord() returns the Unicode code point for a one-character string.)
    """
    cv2.imwrite('lena_copy.png', img)
    """
    Syntax: cv2.imwrite(filename, image)

    Parameters:

    filename: A string representing the file name.
    The filename must include image format like .jpg, .png, etc.

    image: It is the image that is to be saved.

    Return Value: It returns true if image is saved successfully.
    """
    cv2.destroyAllWindows()

"""
Warning:

If you are using a 64-bit machine,
you will have to modify k = cv2.waitKey(0) line
as follows : k = cv2.waitKey(0) & 0xFF
"""
