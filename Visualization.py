from Vector import *
import matplotlib.pyplot as plt
import numpy as np

class Visualization:
  colors = ['k', 'r', 'c', 'y', 'b', 'm', 'g']
  @staticmethod
  def draw_plot(vectors: list[Vector], size: int, ax=None, color=False):
    if not ax:
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

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
  @staticmethod
  def draw_plot3d(vectors: list[Vector], size: int, color=False):
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

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

  @staticmethod
  def visualize(initial_vector: Vector, transformed_vectors: list[Vector]):
    fig, axs = plt.subplots(2, 3)

    axs = np.ndarray.flatten(axs) # got axes in one array, not 2 dimentional
  
    for ax in axs:
      if (len(transformed_vectors) == 0):
        ax.axis('off') # clear unnecessary cells
        continue
      Visualization.draw_plot([initial_vector, transformed_vectors.pop(0)], 8, ax, True)

    plt.show()
