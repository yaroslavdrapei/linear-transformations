from Vector import *
import matplotlib.pyplot as plt
# import numpy as np

class Visualization:
  colors = ['k', 'r', 'c', 'y', 'b', 'm', 'g']
  @staticmethod
  def visualize(vectors: list[Vector], size: int, color=False):
    fig = plt.figure()
    ax = fig.add_subplot()

    for i, vector in enumerate(vectors):
      ax.quiver(0, 0, *vector, 
                 color=Visualization.colors[i % len(Visualization.colors)] if color else 'k', 
                 angles='xy', 
                 scale_units='xy', 
                 scale=1)

    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.grid()

    plt.show()

  def visualize3d(vectors: list[Vector], size: int, color=False):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i, vector in enumerate(vectors):
      ax.quiver(
        0, 0, 0,
        *vector,
        color=Visualization.colors[i % len(Visualization.colors)] if color else 'k'
      )

    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.set_zlim(-size, size)
    ax.grid()

    # Show the plot
    plt.show()