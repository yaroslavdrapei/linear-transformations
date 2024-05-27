import cv2
import numpy as np
import matplotlib.pyplot as plt
from enums import Axis
from LinearTransfomations import LinearTransformations as lt
from Vector import *  
from Matrix import *
from math import ceil
from Visualization import Visualization as V

def mirror_image(image: list[list[list[int]]], axis: Axis):
  result = [[[0 for _ in range(3)] for _ in range(len(image[0]))] for _ in range(len(img))]

  for i, row in enumerate(image):
    for j, col in enumerate(image[i]):
      match axis:
        case Axis.x:
          result[i][j] = image[len(image)-1-i, j]
        case Axis.y:
          result[i][j] = image[i, len(image[i])-1-j]
        case Axis.all:
          result[i][j] = image[len(image)-1-i, len(image[i])-1-j]

  result = np.array(result)
  result = result.astype(np.uint8)

  return result

def scale_in_2_image(image: list[list[list[int]]]):
  result = [[[0 for _ in range(3)] for _ in range(len(image[0]))] for _ in range(len(img))]
  scaled = [[[0 for _ in range(3)] for _ in range(ceil(len(image[0])/2))] for _ in range(ceil(len(image)/2))]

  for i in range(ceil(len(image)/2)):
    for j in range(ceil(len(image[i])/2)):
      # scaled[-1].append(image[i, j])
      scaled[i][j] = image[i, j]

  pointer_x = 0
  for i in range(len(scaled)):
    pointer_y = 0
    for j in range(len(scaled[i])):
      target = scaled[i][j]
      result[pointer_x][pointer_y] = target
      result[pointer_x][pointer_y+1] = target
      result[pointer_x+1][pointer_y] = target
      result[pointer_x+1][pointer_y+1] = target

      pointer_y += 2
    pointer_x += 2


  result = np.array(result)
  result = result.astype(np.uint8)

  return result

img = cv2.imread('./img/2.jpg')

mirrored = mirror_image(img, Axis.y)

mirrored_lib = cv2.flip(img, 1)

scaled = scale_in_2_image(img)

matrix = cv2.getRotationMatrix2D((0, 0), 0, 2)
scaled_lib = cv2.warpAffine(img, matrix, (0, 0))

V.add_pictures(
  2, 3, [img, mirrored_lib, scaled_lib, img, mirrored, scaled],
  titles=['Original', 'Mirrored liblary', 'Scaled library', 'Original', 'Mirrored mine', 'Scaled mine']      
)
plt.show()