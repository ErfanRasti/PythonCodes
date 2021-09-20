"""In this code we are trying to play a video."""
import cv2

cap = cv2.VideoCapture('Medias/test_video.mp4')


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:

        effect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', effect)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
