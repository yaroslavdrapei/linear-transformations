import cv2
import numpy as np

img = cv2.imread('./img/2.jpg')

h, w, _ = img.shape

cv2.imshow('Original image', img)

m = cv2.getRotationMatrix2D((w/2, h/2), 225, 1)
result = cv2.warpAffine(img, m, (w, h))

cv2.imshow('Rotated 225 deg', result)

m = cv2.getRotationMatrix2D((w/2, h/2), 0, 2)
result = cv2.warpAffine(img, m, (w, h))

cv2.imshow('Scaled x2', result)

flipped = cv2.flip(img, 0)
cv2.imshow('Mirrored OX axis', flipped)
cv2.waitKey(0)