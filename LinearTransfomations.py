from Vector import *
from Matrix import *
from enums import Axis
import math

class LinearTransformations:
  @staticmethod
  def scale(vector: Vector, size: int) -> Vector:
    return Matrix([[size, 0], [0, size]]) * vector
  
  @staticmethod
  def scale3d(vector: Vector, size: int):
    result = Matrix([
      [size, 0, 0],
      [0, size, 0],
      [0, 0, size],
    ]) * vector

    return result
  
  @staticmethod
  def mirror(vector: Vector, axis: Axis) -> Vector:
    elementary_matrix = None
    match (axis):
      case Axis.x:
        elementary_matrix = Matrix([[1, 0], [0, -1]])
      case Axis.y:
        elementary_matrix = Matrix([[-1, 0], [0, 1]])
      case Axis.all:
        elementary_matrix = Matrix([[-1, 0], [0, -1]])

    return elementary_matrix * vector
  
  @staticmethod
  def mirror3d(vector: Vector, axis: Axis) -> Vector:
    elementary_matrix = None
    match (axis):
      case Axis.x:
        elementary_matrix = Matrix([
          [1, 0, 0],
          [0, -1, 0],
          [0, 0, -1]
        ])
      case Axis.y:
        elementary_matrix = Matrix([
          [-1, 0, 0],
          [0, 1, 0],
          [0, 0, -1]
        ])
      case Axis.z:
        elementary_matrix = Matrix([
          [-1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]
        ])
      case Axis.all:
        elementary_matrix = Matrix([
          [-1, 0, 0],
          [0, -1, 0],
          [0, 0, -1]
        ])
      

    return elementary_matrix * vector
  
  @staticmethod
  def rotate(vector: Vector, degrees: int) -> Vector:
    radians = degrees * math.pi / 180

    result = Matrix([
      [math.cos(radians), -math.sin(radians)], 
      [math.sin(radians), math.cos(radians)]
    ]) * vector

    return result
  
  @staticmethod
  def shear(vector: Vector, shear: int, axis: Axis) -> Vector:
    elementary_matrix = None
    match (axis):
      case Axis.x:
        elementary_matrix = Matrix([[1, shear], [0, 1]])
      case Axis.y:
        elementary_matrix = Matrix([[1, 0], [shear, 1]])
      case Axis.xy:
        elementary_matrix = Matrix([[1, shear], [shear, 1]])

    return elementary_matrix * vector
  
  @staticmethod
  def custom(vector: Vector, matrix: Matrix) -> Vector:
    return matrix * vector
