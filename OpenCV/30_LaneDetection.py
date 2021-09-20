"""In this codewe wanna detect a road lane via OpenCV."""
import cv2
import numpy as np
# import matplotlib.pyplot as plt


def regionOfInterest(img, vertices):
    """Select the region of interest."""
    mask = np.zeros_like(img)
    """
    zeros_like(a, dtype=None, order='K', subok=True, shape=None) -> tuple
    Return an array of zeros with the same shape and type as a given array.
    """
    # channelCount = img.shape[2]
    """
    It creates a tuple that the number of its arguments are equal with
    channelCount.(The color code indicates white.)
    like: (255,255,...,255)
    """
    # matchMaskColor = (255,) * channelCount
    matchMaskColor = (255,)
    print("matchMaskColor: ", matchMaskColor)

    cv2.fillPoly(mask, vertices, matchMaskColor)
    """fillPoly(img, pts, color[, lineType[, shift[, offset]]]) -> img ."""
    maskedImage = cv2.bitwise_and(img, mask)
    return maskedImage


def drawTheLines(img, lines):
    """Draw the lines."""
    img = np.copy(img)
    blankImage = np.zeros((img.shape), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blankImage, (x1, y1), (x2, y2), (255, 0, 0), thickness=10)

    img = cv2.addWeighted(img, .8, blankImage, 1, 0.0)
    return img


def process(image):
    """Process the image."""
    print(image.shape)
    height, width, _ = image.shape

    regionOfInterestVertices = [
        (0, height), (width/2, height/2), (width, height)]
    """It's a triangle that covers the road."""

    """We write grayImage and cannyImage before croppedImage to prevent
    detecting the edges of the regionOfInterest."""
    grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cannyImage = cv2.Canny(grayImage, 100, 120)

    croppedImage = regionOfInterest(
        cannyImage, np.array([regionOfInterestVertices], np.int32))

    lines = cv2.HoughLinesP(croppedImage,
                            rho=2,
                            theta=np.pi/60,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)

    imageWithLines = drawTheLines(image, lines)
    return imageWithLines

# image = cv2.imread("Medias/road1.png")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


cap = cv2.VideoCapture("Medias/test_video.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is True:
        frame = process(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
