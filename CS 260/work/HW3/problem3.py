#!/usr/bin/python

import timeit
import problem1
import problem2


def main():

	global n
	for n in range(1, 30+1):
		t1 = timeit.Timer('problem1.fib_rec(__main__.n)','import problem1;import __main__')
		delta1 = t1.timeit(1)

		t2 = timeit.Timer('problem2.fib_memo(__main__.n)', 'import problem2; import __main__')
		delta2 = t2.timeit(1)

		print (str(n) + " " + str(delta1) + " " + str(delta2))
	
	f = open('mydata.txt','w')

	global r
	for r in range(1, 100):

		t2 = timeit.Timer('problem2.fib_memo(__main__.r)', 'import problem2; import __main__')
		delta2 = t2.timeit(1)
		f.write( str(r) + " "  + str(delta2) + '\n')

	f.close()

if __name__ == "__main__" : main()
