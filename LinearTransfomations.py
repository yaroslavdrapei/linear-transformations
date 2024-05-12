from Vector import *
from Matrix import *
from enums import Axis
import math

class LinearTransformations:
  @staticmethod
  def scale(vector: Vector, size: int) -> Vector:
    result = vector * Matrix([[size, 0], [0, size]])
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
  
  @staticmethod
  def rotate(vector: Vector, degrees: int) -> Vector:
    radians = degrees * math.pi / 180

    result = vector * Matrix([
      [math.cos(radians), -math.sin(radians)], 
      [math.sin(radians), math.cos(radians)]
    ])

    return Vector(result.matrix)
  
  @staticmethod
  def shear(vector: Vector, shear: int, axis: Axis) -> Vector:
    elementary_matrix = None
    match (axis):
      case Axis.x:
        elementary_matrix = Matrix([[1, 0], [shear, 1]])
      case Axis.y:
        elementary_matrix = Matrix([[1, shear], [0, 1]])
      case Axis.xy:
        elementary_matrix = Matrix([[1, shear], [shear, 1]])
    result = vector * elementary_matrix
    return Vector(result.matrix)
  
  @staticmethod
  def custom(vector: Vector, matrix: Matrix) -> Vector:
    result = vector * matrix
    return Vector(result.matrix)
