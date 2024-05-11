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
    return Vector(vector*Matrix([size, 0], [0, size]))
  
  @staticmethod
  def mirror(vector: Vector, axis: Axis) -> Vector:
    match (axis):
      case Axis.x:
        return Vector(vector * Matrix([[-1, 0], [0, 1]]))
      case Axis.y:
        return Vector(vector * Matrix([[1, 0], [0, -1]]))
      case Axis.xy:
        return Vector(vector * Matrix([[-1, 0], [0, -1]]))