from Visualization import Visualization as V
from math import sin, cos, pi
import numpy as np

initial_vector = np.array([2, 3])
radians = 270 * pi / 180

transformed_vectors = [
  np.dot(initial_vector, np.array([[2, 0], [0, 2]])), # scale
  np.dot(initial_vector, np.array([[-1, 0], [0, 1]])), # mirror
  np.dot(initial_vector, np.array([[1, 0], [0, -2]])), # custom
  np.dot(initial_vector, np.array([[cos(radians), -sin(radians)], [sin(radians), cos(radians)]])), # rotate
  np.dot(initial_vector, np.array([[1, 0], [2, 1]])) # shear
]

V.visualize(2, 3, initial_vector, transformed_vectors, 8)