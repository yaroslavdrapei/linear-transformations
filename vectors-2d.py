from LinearTransfomations import LinearTransformations as lt
from enums import Axis
from Visualization import Visualization as V
from Matrix import Matrix
from Vector import Vector

initial_vector = Vector([2, 3])

transformed_vectors = [
  lt.scale(initial_vector, 2),
  lt.mirror(initial_vector, Axis.y),
  lt.custom(initial_vector, Matrix([[1, 0], [0, -2]])),
  lt.rotate(initial_vector, 270),
  lt.shear(initial_vector, 2, Axis.x),
]

V.visualize(2, 3, initial_vector, transformed_vectors, 8)