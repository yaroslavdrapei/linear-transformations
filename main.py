from LinearTransfomations import *
from Vector import *
from Visualization import *
import matplotlib.pyplot as plt

a = Vector([1, 2])

vectors = [
  a,
  LinearTransformations.scale(a, 3),
  LinearTransformations.mirror(a, Axis.x),
  LinearTransformations.mirror(a, Axis.y),
  LinearTransformations.mirror(a, Axis.xy),
]

Visualization.visualize(vectors, 10)