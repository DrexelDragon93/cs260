#!/usr/bin/python

import cell
import sys

# This function concatentates the two functions but copys values rather than
# assign pointers
def list_concat_copy(A,B):
	C = cell.Cell(A.data)
	tmp = C	
	while A.next != None:
		A = A.next
		tmp.next = cell.Cell(A.data)
		tmp = tmp.next
	
	tmp.next = cell.Cell(B.data)
	tmp = tmp.next
	while B.next != None:
		B = B.next
		tmp.next = cell.Cell(B.data)
		tmp = tmp.next
	return C
	


def main():
	# default lists
	A= cell.Cell(1,cell.Cell(2,cell.Cell(3,cell.Cell(4,cell.Cell(5,None)))))
	print A
	B = cell.Cell(6,cell.Cell(7,cell.Cell(8,cell.Cell(9,cell.Cell(10,None)))))
	print B
	
	# concate function and print
	C = list_concat_copy(A,B)
	print C.__str__()

	# second concate function
	B.next = cell.Cell(6, cell.Cell(7, cell.Cell(8, cell.Cell(9, cell.Cell(10, cell.Cell(11, None))))))
	print C


if __name__ == '__main__':main()
