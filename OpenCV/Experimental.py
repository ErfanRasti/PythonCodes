import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Medias/messi5.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("Medias/messi_face.jpg", 0)
h, w = template.shape
print(template.shape)
