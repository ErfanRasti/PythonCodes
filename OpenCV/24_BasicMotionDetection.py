"""In this code we wanna detect the persons who walk in the video."""
import cv2
# import numpy as np
# import matplotlib.pyplot as plt

cap = cv2.VideoCapture("Medias/vtest.avi")

ret, frame1 = cap.read()
ret, frame2 = cap.read()


while cap.isOpened() and ret is True:

    diff = cv2.absdiff(frame1, frame2)
    """absdiff(src1, src2[, dst]) -> dst"""
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        """boundingRect(array) -> retval"""
        if cv2.contourArea(contour) < 850:
            """contourArea(contour[, oriented]) -> retval"""
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
            cv2.putText(frame1, f"Status:{'Movement'}", (10, 20),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 0, 255),
                        thickness=1)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
