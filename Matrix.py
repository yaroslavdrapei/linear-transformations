import numpy as np

class Matrix:
  def __init__(self, matrix: list[list[int]]):
    self.matrix = np.array(matrix)
    self.rows = len(self.matrix)
    self.cols = len(self.matrix[0])
  
  @staticmethod
  def __multiply_lists(l1, l2):
    return sum([l1[i] * l2[i] for i in range(len(l1))])
  
  @staticmethod
  def __get_col(matrix, index):
    return [matrix[i][index] for i in range(len(matrix))]
  
  def __str__(self):
    result = ''
    for row in self.matrix:
      result += ' '.join([str(i) for i in row]) + '\n'
    return result.strip()

  def __mul__(self, other):
    if (self.cols != other.rows):
      raise Exception(f'Multiplication is impossible! {self.rows}x{self.cols} {other.rows}x{other.cols}')
    
    result = [[None for _ in range(other.cols)] for _ in range(self.rows)]
    
    for i in range(self.rows):
      for j in range(other.cols):
        result[i][j] = Matrix.__multiply_lists(self.matrix[i], Matrix.__get_col(other.matrix, j))
    
    return Matrix(result)