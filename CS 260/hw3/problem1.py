#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 3
# Sample Solution

from fibonacci import fib_rec
import sys

def main():
  if len(sys.argv) != 2:
    print "Must provide one argument n."
    return

  print fib_rec(int(sys.argv[1]))

if __name__ == "__main__":
  main()

