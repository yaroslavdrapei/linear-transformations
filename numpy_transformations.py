from Visualization import Visualization as V
from math import sin, cos, pi
import numpy as np

initial_vector = np.array([2, 3])
radians = 270 * pi / 180

transformed_vectors = [
  np.dot(np.array([[2, 0], [0, 2]]), initial_vector), # scale
  np.dot(np.array([[-1, 0], [0, 1]]), initial_vector), # mirror
  np.dot(np.array([[1, 0], [0, -2]]), initial_vector), # custom
  np.dot(np.array([[cos(radians), -sin(radians)], [sin(radians), cos(radians)]]), initial_vector), # rotate
  np.dot(np.array([[1, 2], [0, 1]]), initial_vector) # shear
]

for vector in transformed_vectors:
  print(vector)

V.visualize(2, 3, initial_vector, transformed_vectors, 8)