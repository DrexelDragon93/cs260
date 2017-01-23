#!/usr/bin/env python

import sys
from graph import Matrix, Graph

def Floyd(G):
  """
  Given a graph G, return the final distance matrix A and the predecessor
  matrix P 
  """

  # init cost matrix C
  C = G.matrix
  
  # init distance matrix A and predecessor matrix P
  A = Matrix(C.n)
  P = Matrix(C.n)
  for i in range(C.n):
    for j in range(C.n):
      A.set(i, j, C.get(i, j))
      P.set(i, j, 0)

  for i in range(A.n):
    A.set(i, i, 0)

  for k in range(A.n):
    for i in range(A.n):
      for j in range(A.n):
        ik = A.get(i, k)
        kj = A.get(k, j)
        ij = A.get(i, j)
        #print "ik: %s, kj: %s, ij: %s" % (ik, kj, ij)
        
        # infinite path through k can't be shorter
        if ik is None or kj is None:
          continue
        
        # see if path through k is shorter
        if ik + kj < ij:
          A.set(i, j, ik + kj)
          P.set(i, j, k)

  return (A, P)

def load_graph():
  """
  Load graph from stdin
  """

  lines = sys.stdin.readlines()
  G = Graph(len(lines))

  for line in lines:
    tokens = line.split()
    v = int(tokens[0])

    for t in tokens[1:]:
      w, c = map(int, t.split(","))
      G.add_edge(v, w, c)

  return G

def main():
  G = load_graph()
  #G.show()
  #print
  
  A, P = Floyd(G)

  A.show()
  print
  P.show()

if __name__ == "__main__":
  main()

