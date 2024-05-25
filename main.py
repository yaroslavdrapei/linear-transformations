from LinearTransfomations import LinearTransformations as lt
from enums import *
from Visualization import *

a = Vector([5, 6, 6]) 

vectors = [
  a,
  lt.scale3d(a, 1.5),
  lt.mirror3d(a, Axis.z)
]

Visualization.visualize3d(vectors, 10, True)