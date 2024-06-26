from Matrix import *
import numpy as np

class Vector(Matrix):
  def __init__(self, vector):
    super().__init__(np.array([[coord] for coord in vector]))
    self.vector = np.ndarray.flatten(np.array(vector))

  def __getitem__(self, index):
    return self.vector[index]
  
  def __str__(self):
    return ' '.join([str(coord) for coord in self.vector])
  
  def __mul__(self, other):
    product = super().__mul__(other)
    return Vector(product.matrix)
  