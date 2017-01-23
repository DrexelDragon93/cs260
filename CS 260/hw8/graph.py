#!/usr/bin/env python

class Matrix:
  def __init__(self, n):
    self.n = n
    self.cells = [None] * (n * n)

  def set(self, i, j, x):
    self.cells[self.n * i + j] = x

  def get(self, i, j):
    return self.cells[self.n * i + j]

  def show(self):
    """
    Print the matrix to stdout
    """

    COL_WIDTH = 4
    
    # print col header
    print " " * COL_WIDTH,
    for i in range(self.n):
      print repr(i).rjust(COL_WIDTH),
    print

    # print rows
    for i in range(self.n):
      # print row header
      print repr(i).rjust(COL_WIDTH),

      # print values
      for j in range(self.n):
        v = self.get(i, j)
        if v is not None:
          print repr(v).rjust(COL_WIDTH),
        else:
          print "INF".rjust(COL_WIDTH),
      
      print

class Graph:
  """
  Undirected Graph
  """

  def __init__(self, n):
    """
    Create graph with vertices [0..(n-1)]
    """
    self.matrix = Matrix(n)

  def add_edge(self, v, w, c):
    """
    Add undirected edge between vertices v and w with cost c
    """

    self.matrix.set(v, w, c)
    self.matrix.set(w, v, c)

  def remove_edge(self, v, w):
    """
    Remove undirected edge between vertices v and w
    """

    self.matrix.set(v, w, None)
    self.matrix.set(w, v, None)

  def show(self):
    self.matrix.show()

def main():
  G = Graph(5)
  G.add_edge(1, 3, 20)
  G.show()
  
  print
  G.remove_edge(1, 3)
  G.show()

if __name__ == "__main__":
  main()

