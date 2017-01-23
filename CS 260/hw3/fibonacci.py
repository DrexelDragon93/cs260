#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 3
# Sample Solution

def fib_rec(n):
  """
  Recursive fibonacci
  """

  if n <= 2:
    return 1

  return fib_rec(n - 1) + fib_rec(n - 2)

def fib_memo(n):
  """
  Recursive fibonacci with memoization

  Since cache is zero-indexed, we will use index [n - 1] for the nth number
  """

  if n <= 2:
    return 1 # don't bother caching

  cache = fib_memo.cache[n - 1]

  if cache != 0:
    return cache

  val = fib_memo(n - 1) + fib_memo(n - 2)
  fib_memo.cache[n - 1] = val
  return val

fib_memo.cache = [0 for x in range(100)]

def main():
  """
  Test driver
  """

  print [fib_rec(x) for x in range(1, 11)]
  print [fib_memo(x) for x in range(1, 11)]

if __name__ == "__main__":
  main()

