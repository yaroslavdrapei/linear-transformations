from Vector import *
import matplotlib.pyplot as plt
import numpy as np

class Visualization:
  colors = ['k', 'r', 'c', 'y', 'b', 'm', 'g']
  @staticmethod
  def draw_plot(vectors: list[Vector], size: int, ax, color=False):
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
  def draw_plot3d(vectors: list[Vector], size: int, ax, color=False):
    if not ax:
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
  def visualize(rows: int, cols: int, initial_vector: Vector, transformed_vectors: list[Vector], size: int):
    fig = plt.figure()
  
    for i, vector in enumerate(transformed_vectors):
      ax = fig.add_subplot(rows, cols, i+1)
      Visualization.draw_plot([initial_vector, vector], size, ax, True)

    plt.show()

  def visualize3d(rows: int, cols: int, initial_vector: Vector, transformed_vectors: list[Vector], size: int):
    fig = plt.figure()
  
    for i, vector in enumerate(transformed_vectors):
      ax = fig.add_subplot(rows, cols, i+1, projection='3d')
      Visualization.draw_plot3d([initial_vector, vector], size, ax, True)

    plt.show()
