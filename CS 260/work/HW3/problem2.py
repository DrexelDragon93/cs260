#!/usr/bin/python

import problem1
import problem3
mem_list = [None] * 100

def fib_memo(n):
	global mem_list
	mem_list = mem_list
	if n < 2:
		return 1
	elif mem_list[n] != None:
		return mem_list[n]
	else:
		mem_list[n] = fib_memo(n-1) + fib_memo(n-2)
		return mem_list[n]


def main():
	size = 100

	global mem_list

	for x in range(0,10):
		print fib_memo(x)


if __name__ == "__main__" : main()
