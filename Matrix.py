class Matrix:
  def __init__(self, matrix: list[list[int]]):
    self.matrix = matrix
    self.rows = len(matrix)
    self.cols = len(matrix[0])
  
  def __multiply_lists(self, l1: list, l2: list):
    return sum([l1[i] * l2[i] for i in range(len(l1))])

  def __get_col(self, matrix, index):
    return [matrix[i][index] for i in range(len(matrix))]
  
  def __str__(self):
    result = ''
    for row in self.matrix:
      result += ' '.join([str(i) for i in row]) + '\n'
    return result.strip()

  def __mul__(self, other):
    if (self.cols != other.rows):
      raise Exception('Multiplication is impossible!')
    
    result = [[None for _ in range(other.cols)] for _ in range(self.rows)]
    
    for i in range(self.rows):
      for j in range(other.cols):
        result[i][j] = self.__multiply_lists(self.matrix[i], self.__get_col(other.matrix, j))
    
    return Matrix(result)