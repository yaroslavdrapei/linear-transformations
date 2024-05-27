from LinearTransfomations import LinearTransformations as lt
from Visualization import Visualization as V
from Matrix import Matrix
from Vector import Vector

initial_vector = Vector([2, 2])

custom_matrix = Matrix([
  [1, 0],
  [0, -2]
])

rotated = lt.rotate(initial_vector, 90)
customed = lt.custom(initial_vector, custom_matrix)

transformed_vectors = [
  lt.custom(rotated, custom_matrix),
  lt.rotate(customed, 90),
]

V.visualize(1, 2, initial_vector, transformed_vectors, 4)