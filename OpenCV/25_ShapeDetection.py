"""In this code we wanna detect some shapes using contours."""
import cv2
# import numpy as np

img = cv2.imread("Medias/Shapes2.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, thresh = cv2.threshold(grayImg, 20, 255, cv2.THRESH_BINARY)
canny = cv2.Canny(grayImg, 255, 255)
contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for contour in contours:
    approx = cv2.approxPolyDP(
        curve=contour, epsilon=0.01*cv2.arcLength(contour, closed=True),
        closed=True)
    """approxPolyDP(curve, epsilon, closed[, approxCurve]) -> approxCurve """
    """
    arcLength(curve, closed) -> retval .
    @brief Calculates a contour perimeter or a curve length. . .
    The function computes a curve length or a closed contour perimeter
    """

    if cv2.contourArea(contour) < 200000:
        """I use this condition to prevent creating big contour all around
        the screen."""
        cv2.drawContours(img, [approx], 0, (200, 0, 0), thickness=5)

        x = approx.ravel()[0]
        y = approx.ravel()[1]-5

        if len(approx) == 3:
            cv2.putText(img, "Triangle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))

        elif len(approx) == 4:
            _, _, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h

            if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                cv2.putText(img, "square", (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))
            else:
                cv2.putText(img, "rectangle", (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))

        elif len(approx) == 5:
            cv2.putText(img, "Pentagon", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))

        elif len(approx) == 10:
            cv2.putText(img, "Star", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))

        else:
            cv2.putText(img, "Circle", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 200))


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
