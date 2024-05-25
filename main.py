from LinearTransfomations import LinearTransformations as lt
from enums import *
from Visualization import *

a = Vector([2, 2])  

vectors = [
  a,
  lt.scale(a, 3),
  lt.mirror(a, Axis.y),
  lt.custom(a, Matrix([[1, 0], [0, -2]])),
  lt.rotate(a, 270),
  lt.shear(a, 2, Axis.x)
]

print(lt.shear(a, 2, Axis.x))

# Visualization.visualize(vectors, 8, True)

vectors3d = [
  Vector([3, 2, 4]),
  Vector([4, 1, 0]),
  Vector([6, 0, 0]),
]

Visualization.visualize3d(vectors3d, 6, True)