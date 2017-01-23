#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 2
# Sample Solution

import argparse
import cell
import listconcat
import timeit

def create_list(n):
  """
  Create a list with n elements
  """

  L = None
  for i in xrange(n):
    L = cell.Cell(1, L)

  return L

n = None
def main():

  setup = """
import cell
from listconcat import list_concat, list_concat_copy
from __main__ import n, create_list
A = create_list(n)
B = create_list(n)
"""

  global n
  for n in xrange(100, 10000 + 1, 100):

    time_nocopy = timeit.timeit("list_concat(A, B)", setup=setup, number = 1)
    time_copy = timeit.timeit("list_concat_copy(A, B)", setup=setup, number = 1)
  
    print "%d %f %f" % (n, time_nocopy, time_copy)

if __name__ == "__main__":
  main()

