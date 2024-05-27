import cv2
import matplotlib.pyplot as plt
from Visualization import Visualization as V

img = cv2.imread('./img/2.jpg')

height, width, _ = img.shape

matrix = cv2.getRotationMatrix2D((width/2, height/2), 225, 1)
rotated = cv2.warpAffine(img, matrix, (width, height))

matrix = cv2.getRotationMatrix2D((0, 0), 0, 2)
scaled = cv2.warpAffine(img, matrix, (width, height))

mirrored = cv2.flip(img, 0)

pictures = [img, rotated, scaled, mirrored]

V.add_pictures(2, 2, pictures, ['Original', 'Rotated', 'Scaled', 'Mirrored by OX'])

plt.show()