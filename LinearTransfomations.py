from Vector import *
from enum import Enum
import math

class Axis(Enum):
  x = 0
  y = 1
  xy = 2

class LinearTransformations:
  @staticmethod
  def scale(vector: Vector, size: int) -> Vector:
    result = vector*Matrix([[size, 0], [0, size]])
    return Vector(result.matrix)
  
  @staticmethod
  def mirror(vector: Vector, axis: Axis) -> Vector:
    elementary_matrix = None
    match (axis):
      case Axis.x:
        elementary_matrix = Matrix([[1, 0], [0, -1]])
      case Axis.y:
        elementary_matrix = Matrix([[-1, 0], [0, 1]])
      case Axis.xy:
        elementary_matrix = Matrix([[-1, 0], [0, -1]])
    result = vector * elementary_matrix
    return Vector(result.matrix)