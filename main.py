from LinearTransfomations import LinearTransformations as lt
from enums import *
from Visualization import *

a = Vector([1, 2, 1]) 

vectors = [
  a,
  lt.scale3d(a, 2)
]

Visualization.visualize3d(vectors, 10, True)