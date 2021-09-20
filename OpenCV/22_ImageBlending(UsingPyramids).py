"""
In this code we wanna blend two images using pyramids.

Steps:
1. Load the two images of apple and orange
2. Find the Gaussian Pyramids for apple and orange
(in this particular example, number of levels is 6)
3. From Gaussian Pyramids, find their Laplacian Pyramids
4. Now join the left half of apple and right half of orange
in each levels of Laplacian Pyramids
5. Finally from this joint image pyramids, reconstruct the original image.
"""
import cv2
import numpy as np
# import matplotlib.pyplot as plt

"""Number of layers"""
k = 6


# step 1
apple = cv2.imread("Medias/apple.jpg")
orange = cv2.imread("Medias/orange.jpg")
print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))


# step 2
"""Generate Gaussian pyramid of apple."""
apple_layer = apple.copy()
gp_apple = [apple_layer]
for i in range(k):
    apple_layer = cv2.pyrDown(apple_layer)
    gp_apple.append(apple_layer)

"""Generate Gaussian pyramid of apple."""
orange_layer = orange.copy()
gp_orange = [orange_layer]
for i in range(k):
    orange_layer = cv2.pyrDown(orange_layer)
    gp_orange.append(orange_layer)


# step 3
"""Generate Laplacian pyramid of apple."""
apple_layer = gp_apple[-1]
lp_apple = [apple_layer]
for i in range(k, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

"""Generate Laplacian pyramid of orange."""
orange_layer = gp_orange[-1]
lp_orange = [orange_layer]
for i in range(k, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)


# step 4
"""Add left and right halves of images in each level."""
apple_orange_pyramid = list()
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack(
        ((apple_lap[:, :int(cols/2)]), (orange_lap[:, int(cols/2):])))
    apple_orange_pyramid.append(laplacian)


# step 5
"""Reconstruct image."""
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, k+1):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(
        apple_orange_reconstruct, apple_orange_pyramid[i])
    """add(src1, src2[, dst[, mask[, dtype]]]) -> dst"""

titles = ["apple", "orange", "apple_orange", "apple_orange_reconstruct"]
images = [apple, orange, apple_orange, apple_orange_reconstruct]


# for i in range(len(images)):
#     plt.subplot(2, 2, i+1)
#     cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
#     plt.imshow(images[i], "gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])

# plt.show()


cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    pass
elif k == ord('s'):
    cv2.imwrite("apple_orange.png", apple_orange)
    cv2.imwrite("apple_orange_reconstruct.png", apple_orange_reconstruct)

cv2.destroyAllWindows()
