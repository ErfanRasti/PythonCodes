"""
Canny Edge Detection is a popular edge detection algorithm.\
It was developed by John F. Canny in 1986.

The Canny edge detection algorithm is composed of 5 steps:
1. Noise Reduction
2. Gradient Calculation
3. Non-maximum Supperession
4. Double Threshold
5. Edge Tracking by Hysteresis
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard


def nothing(nothing):
    """Pass nothing for trackbars."""
    pass


img = cv2.imread('Medias/messi5.jpg', 0)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

"""Creating a trackbar for setting thresholds"""
cv2.namedWindow('Trackbars')
cv2.createTrackbar('Threshold1', 'Trackbars', 100, 255, nothing)
cv2.createTrackbar('Threshold2', 'Trackbars', 200, 255, nothing)
trackbars = np.zeros((1, 512, 3), np.uint8)
cv2.imshow('Trackbars', trackbars)


titles = ['Image', 'Laplacian', 'Sobel X',
          'Sobel Y', 'Sobel Combined', 'Canny']

while(1):

    canny = cv2.Canny(img, cv2.getTrackbarPos('Threshold1', 'Trackbars'),
                      cv2.getTrackbarPos('Threshold2', 'Trackbars'))
    images = [img, lap, sobelX, sobelY, sobelCombined, canny]
    for i in range(len(images)):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show(block=False)
    k = plt.waitforbuttonpress(1)
    if keyboard.is_pressed('esc'):
        plt.close()
        break
