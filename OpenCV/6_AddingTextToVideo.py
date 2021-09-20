"""In this code we are trying to add text to out video."""
import cv2
import datetime

cap = cv2.VideoCapture(0)
print('Frame Width: ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame Height: ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 800)
cap.set(4, 800)
cap.set(10, 150)
cap.set(11, 150)
cap.set(cv2.CAP_PROP_FRAME_COUNT, 0)

print('Frame Width: ', cap.get(3))
print('Frame Height: ', cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        frame = cv2.flip(frame, 1)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + '   ' + \
            'Height: ' + str(cap.get(4))

        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, text, (10, 50), font, 0.5,
                            (0, 255, 255), 1, cv2.LINE_AA)
        """ This line writes the size of our frame."""

        frame = cv2.putText(frame, datet, (10, 70), font, 0.5,
                            (0, 0, 255), 1, cv2.LINE_AA)
        """This line writes the datetime."""

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
