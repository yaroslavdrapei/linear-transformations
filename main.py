from LinearTransfomations import LinearTransformations as lt
from enums import *
from Visualization import *

a = Vector([1, 2])

vectors = [
  a,
  lt.scale(a, 3),
  lt.mirror(a, Axis.x),
  lt.mirror(a, Axis.y),
  lt.mirror(a, Axis.xy),
]

Visualization.visualize(vectors, 10)