#!/usr/bin/python

import sys


def main():
	dictionary = {}
	
	#open the set file path
	with open('example.input') as f:

	
	# parse into dictionary
		for line in f:
			tmp = line.strip('\n')
			tmp = tmp.split(" ")
	
			dictionary[tmp[0]] = tmp[1:]			
		size = len(dictionary)

		mylist = [[0 for x in xrange(size)] for x in xrange(size)] 

	# read and split dictionary furthur
		currentValue =""
		for keys in dictionary:
			l = dictionary[keys]
			for values in l:
				currentValue = values.split(",")
			
				if currentValue[0] != '':
					if currentValue[1] == 'inf':
						currentValue[1] = 999999999;
					mylist[int(keys)][int(currentValue[0])] = currentValue[1]
					mylist[int(currentValue[0])][int(keys)] = currentValue[1]

		# get two matrix
		(d,n) = floydsAlg(mylist)


		#display
		print
		print "Distance Matrix - D"
		print
		#printMatrix(mylist)
		printMatrix(d)
		print
		print
		print "Predecessor Matrix - P"
		print
		printMatrix(n)



# print the matrix
def printMatrix(mylist):
	
	for i in range(0,len(mylist)):
		for j in range(0,len(mylist)):
			if mylist[i][j] == 999999999:
				print repr('inf').ljust(2),
			else:
				print repr(int(mylist[i][j])).ljust(2),
		print
	
# floyds alg
def floydsAlg(mylist):
	
	A = [[0 for x in xrange(len(mylist))] for x in xrange(len(mylist))]
	nextVar = [[0 for x in xrange(len(mylist))] for x in xrange(len(mylist))]

	for i in range(0,len(mylist)):
		for j in range(0,len(mylist)):
			A[i][j] = mylist[i][j]
			nextVar[i][j] = j

#	for i in range(0,len(mylist)):
#		A[i][i] = 0
	
	for k in range(0,len(mylist)):
		for i in range(0,len(mylist)):
			for j in range(0,len(mylist)):

				if int(A[i][k]) + int(A[k][j]) < int(A[i][j]) :
					A[i][j] = int(A[i][k]) + int(A[k][j])	
					nextVar[i][j] = nextVar[i][k]
	
	return (A,nextVar)


	



if __name__== "__main__" : main()




