#!/usr/bin/python

import timeit
import cell
import problem1
import problem2




def create_list(n):
	C = cell.Cell(1)
	for x in range(n):
		C = cell.Cell(x, C)
	return C



# The main function
def main():
	
	# open a new file for data storage
	f = open('mydata.txt', 'w')

	# lets the program no to use global variable
	global n
	for n in range(100, 10000+1, 100):
		t1 = timeit.Timer('problem1.list_concat(__main__.create_list(__main__.n),__main__.create_list(__main__.n))', 'import cell; import __main__; import problem1; import problem2')
	
		
		t2 = timeit.Timer('problem2.list_concat_copy(__main__.create_list(__main__.n),__main__.create_list(__main__.n))', 'import cell; import __main__; import problem1; import problem2')
	
		delta1 = t1.timeit( 1 )
		delta2 = t2.timeit( 1 )
		f.write(  str(n) + "  " + str( delta1 ) + " " + str( delta2 ) + "\n" )

	# close the open file
	f.close()

# tells program where to start
if __name__=="__main__": main()
