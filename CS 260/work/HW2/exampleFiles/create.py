#!/usr/bin/python

import cell
import problem1
import problem2

global n

def create_list(n):
   C = cell.Cell(1)
   for x in range(n):
      C = cell.Cell(x, C)
   return C


