"""In this file we wanna capture a video via our webcam."""

import cv2


cap = cv2.VideoCapture(0)
"""
To capture a video, you need to create a VideoCapture object.
Its argument can be either the device index or the name of a video file.
Device index is just the number to specify which camera.
Normally one camera will be connected (as in my case).
So I simply pass 0 (or -1).
You can select the second camera by passing 1 and so on.
After that, you can capture frame-by-frame. But at the end,
don’t forget to release the capture.
"""

# Define the codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'XVID')
"""
FourCC is a 4-byte code used to specify the video codec.
The list of available codes can be found in fourcc.org.
It is platform dependent. Following codecs works fine for me.

In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2.
(XVID is more preferable.
MJPG results in high size video.
X264 gives very small size video)

In Windows: DIVX (More to be tested and added)

In OSX : (I don’t have access to OSX. Can some one fill this?)

FourCC code is passed as cv2.VideoWriter_fourcc('M','J','P','G')
or cv2.VideoWriter_fourcc(*'MJPG) for MJPG.
"""

out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
"""
VideoWriter object is used for saving a video.
We should specify the output file name (eg: output.avi).
Then we should specify the FourCC code.
Then number of frames per second (fps) and frame size should be passed.
And last one is isColor flag. If it is True, encoder expect color frame,
otherwise it works with grayscale frame.
"""


print('Frame Width: ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame Height: ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
"""
You can also access some of the features of this video
using cap.get(propId) method where propId is a number from 0 to 18.
Each number denotes a property of the video
(if it is applicable to that video) and full details can be seen here:
Property Identifier. Some of these values can be modified
using cap.set(propId, value). Value is the new value you want.

For example, I can check the frame width and height
by cap.get(3) and cap.get(4). It gives me 640x480 by default.
But I want to modify it to 320x240. Just use ret = cap.set(3,320)
and ret = cap.set(4,240).
"""


cap.open(0)
print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()

    """
    cap.read() returns a bool (True/False).
    If frame is read correctly, it will be True.
    So you can check end of the video by checking this return value.

    Sometimes, cap may not have initialized the capture.
    In that case, this code shows error. You can check whether
    it is initialized or not by the method cap.isOpened().
    If it is True, OK. Otherwise open it using cap.open().

    In this case it saves our image in 'frame' variable and
    then it will tell us wether it was done successfully or not.
    'ret' variable is a boolean which is True or False.
    If there is no frame, you wont get an error, you will get None.


    """
    if ret is True:
        """If ret isn't True, we will face with an error.
        So I put an if statement to prevent this problem.
        We can use this lines instead:
        if frame is None:
                break
        """
        frame = cv2.flip(frame, 1)
        """
        Specify the original ndarray as the first argument and
        a value indicating the directions the second argument flipCode.

        The image is flipped according to the value of flipCode as follows:

        flipcode = 0: flip vertically
        flipcode > 0: flip horizontally
        flipcode < 0: flip vertically and horizontally
        """

        out.write(frame)
        """This line save a frame in a video file. (output.avi)"""

        BGR = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        """This method converts an frame from one color space to another."""

        cv2.imshow('frame', BGR)
        """ This function shows the BGR with the name in first argument."""

        if cv2.waitKey(1) & 0xFF == 27:
            """
            We pass 1ms to waitkey to have a time for pressing ESC.
            If we pass 0ms, it will capture only one frame.
            If we pass 10ms or above, it will work slowly.

            0xFF is a hexadecimal constant which is 11111111 in binary.
            By using bitwise AND (&) with this constant, it leaves
            only the last 8 bits of the original
            (in this case, whatever cv2.waitKey(0) is).
            Truthfully in this case you don't need 0xFF.
            If you did cv2.waitkey(0) == ord(q) it would work all the same.
            0xFF is just used to mask off the last 8bits of the sequence and
            the ord() of any keyboard character will not be greater than 255.
            You can reference this ASCII Table to find the numerical values
            of any keyboard character.
            """
            break
    else:
        """If there is no else statement at the end of the video
        it won't run out and it will show the last frame."""
        break
cap.release()
out.release()
"""cap.release() method destroys cap."""
cv2.destroyAllWindows()

"""
See also:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
"""
