from LinearTransfomations import LinearTransformations as lt
from enums import Axis
from Visualization import Visualization as V
from Vector import Vector

initial_vector = Vector([2, 3, 4])

transformed_vectors = [
  lt.scale3d(initial_vector, 3),
  lt.mirror3d(initial_vector, Axis.z),
]

V.visualize3d(1, 2, initial_vector, transformed_vectors, 12)