from Matrix import *
import numpy as np

class Vector(Matrix):
  def __init__(self, vector):
    super().__init__(np.array([vector]))
    self.vector = np.ndarray.flatten(np.array(vector))

  def __getitem__(self, index):
    return self.vector[index]
  