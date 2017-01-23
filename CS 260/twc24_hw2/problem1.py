#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 2
# Sample Solution

import cell
import listconcat

def main():

  # A = 1..5
  A = None
  for i in reversed(xrange(1, 6)):
    A = cell.Cell(i, A)

  print "A:", A

  # B = 6..10
  B = None
  for i in reversed(xrange(6, 11)):
    B = cell.Cell(i, B)

  print "B:", B

  # C = 1..10
  C = listconcat.list_concat(A, B)
  print "C = list_concat(A, B):", C

  # modify B
  end = B
  while end.next is not None:
    end = end.next
  
  end.next = cell.Cell(11)

  # B = 6..11
  print "Modified B:", B

  # C = 1..11
  print "C:", C

if __name__ == "__main__":
  main()

