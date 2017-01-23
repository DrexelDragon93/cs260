#!/usr/bin/python


def fib_rec(n):
	if n < 2:
		return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)

def main():

	for x in range(0,10):
		print fib_rec(x)

if __name__== "__main__" : main()
