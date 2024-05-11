from Matrix import *
import numpy as np

class Vector(Matrix):
  def __init__(self, vector):
    super().__init__(np.array([vector]))
    self.vector = np.array(vector)