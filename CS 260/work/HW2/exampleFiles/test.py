#!/usr/bin/python

import cell
import problem2
import problem1 

A = cell.Cell(8, cell.Cell(10, None))
B = cell.Cell(11, cell.Cell(13, None))
C = problem2.list_concat_copy(A, B)

print problem1.create_list(100)
print C

