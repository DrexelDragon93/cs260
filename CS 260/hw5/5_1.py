#!/usr/bin/env python

from itertools import permutations
from bst import BST

def main():

  values = [1, 2, 3, 4]
  trees = set()

  for p in permutations(values):
    tree = BST()
    for x in p:
      tree.insert(x)
    trees.add("%s" % tree)

  print len(trees)
  for t in trees:
    print t

if __name__ == "__main__":
  main()

