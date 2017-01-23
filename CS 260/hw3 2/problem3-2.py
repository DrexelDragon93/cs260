#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 3
# Sample Solution

import os
import timeit

n = 0
def main():

  setup = """
from __main__ import n
from fibonacci import fib_memo
"""

  global n
  for n in range(1, 101):
    time_memo = timeit.timeit("fib_memo(n)", setup=setup, number = 1)

    print "%d %f" % (n, time_memo)

if __name__ == "__main__":
  main()

