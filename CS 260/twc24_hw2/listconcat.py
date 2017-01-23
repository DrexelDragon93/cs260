#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 2
# Sample Solution

import cell

def list_concat(A, B):
  """
  Concatenate two linked lists A and B without copying the data. Point the last
  cell in A to the first cell in B.
  """
  
  # if either is None, return the other 
  if A is None:
    return B
  if B is None:
    return A

  # find the last cell in A
  last = A
  while last.next is not None:
    last = last.next

  # point the last cell in A to the first cell in B
  last.next = B

  # A is now the concatenated list
  return A

def list_copy(L):
  """
  Return a copy of a linked list
  """

  # if the list is None, return None
  if L is None:
    return None

  # copy the first cell in L and save a reference to it
  temp = cell.Cell(L.data)
  copy = temp

  # copy the rest of the list
  next = L.next
  while next is not None:
    temp.next = cell.Cell(next.data)
    temp = temp.next
    next = next.next

  # return the copied list
  return copy

def list_concat_copy(A, B):
  """
  Concatenate two linked lists A and B, copying the data so A and B remain
  independent.
  """

  # if either is None, return a copy of the other 
  if A is None:
    return list_copy(B)
  if B is None:
    return list_copy(A)

  # copy A first
  C = list_copy(A)
  
  # find the last cell in the copied list
  last = C
  while last.next is not None:
    last = last.next

  # point the last cell in the copy of A to the first cell in a copy of B
  last.next = list_copy(B)

  # C is now the concatenated, copied list
  return C

def main():
  """
  Test driver
  """

  A = cell.Cell(1)
  temp = A
  for i in range(2, 6):
    temp.next = cell.Cell(i)
    temp = temp.next

  print "A:", A

  B = cell.Cell(6)
  temp = B
  for i in range(7, 11):
    temp.next = cell.Cell(i)
    temp = temp.next

  print "B:", B

  C = list_concat_copy(A, B)
  print "list_concat_copy(A, B):", C

  D = list_concat(A, B)
  print "list_concat(A, B):", D

  E = list_concat_copy(A, B)
  print "list_concat_copy(A, B):", E

if __name__ == "__main__":
  main()

