#!/usr/bin/env python
# Tim Cheeseman
# CS 260 Assignment 3
# Sample Solution

from fibonacci import fib_memo

def main():
  for i in [fib_memo(x) for x in range(1, 11)]:
    print i

if __name__ == "__main__":
  main()

