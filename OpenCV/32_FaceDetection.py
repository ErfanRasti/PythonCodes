"""Let's detect our face."""
import cv2
# import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

# Capture the video.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        frame = cv2.flip(frame, 1)
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        """
        detectMultiScale(image[, scaleFactor[, minNeighbors[, flags
        [, minSize[, maxSize]]]]]) -> objects
        @brief Detects objects of different sizes in the input image.
        The detected objects are returned as a list of rectangles.
        """
        faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)

        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            roiGrayImg = grayImg[y:y+h, x:x+h]
            roiColorImg = frame[y:y+h, x:x+h]
            eyes = eyesCascade.detectMultiScale(roiGrayImg)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roiColorImg, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    else:
        break

cap.release()
