#!/usr/bin/python

import sys

class Cell:

	def __init__( self, data, next=None ):
		self.data = data
		self.next = next

	def __str__( self ):
		return "(%s, %s)" % ( self.data, self.next )

	def echo( self ):
		print self.__str__()


def list_concat(A,B):

	C = A
	while A.next != None:
		A = A.next
	A.next = B
	return C
	


def main():

	# List A and B are defined and displayed
	A= Cell(1,Cell(2,Cell(3,Cell(4,Cell(5,None)))))
	print A
	B = Cell(6,Cell(7,Cell(8,Cell(9,Cell(10,None)))))
	print B
	
	# They are concatenated
	C = list_concat(A,B)
	print C
	


if __name__ == '__main__':main()
