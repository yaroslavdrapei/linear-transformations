from Vector import *
import matplotlib.pyplot as plt

class Visualization:
  @staticmethod
  def visualize(vectors: list[Vector], size: int):
    for vector in vectors:
      plt.quiver(0, 0, *vector, angles='xy', scale_units='xy', scale=1)

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    plt.grid()
    plt.show()