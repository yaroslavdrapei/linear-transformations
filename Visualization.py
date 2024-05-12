from Vector import *
import matplotlib.pyplot as plt

class Visualization:
  @staticmethod
  def visualize(vectors: list[Vector], size: int, color=False):
    colors = ['k', 'r', 'c', 'y', 'b', 'm', 'g']
    for i, vector in enumerate(vectors):
      plt.quiver(0, 0, *vector, 
                 color=colors[i % len(colors)] if color else 'k', 
                 angles='xy', 
                 scale_units='xy', 
                 scale=1)

    plt.xlim(-size, size)
    plt.ylim(-size, size)

    plt.grid()
    plt.show()