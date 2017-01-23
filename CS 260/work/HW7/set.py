#!/usr/bin/python

import mfset

def Initialize(Values):
	tmpList = []
	count = 0
	for x in Values:
		tmpList.append(mfset.MFSet( x , None, count ) )
		count = count + 1
	return tmpList

def Find( s, values ):
	

	for x in s:

		if x.label == values:
			return x.name
	return None
	


def Merge( s, value1, value2 ):
		tmp = s[Find( s, value1 )]
		tmp2 = s[Find( s, value2)]
	


	
		if tmp == None or tmp2 == None or tmp == tmp2:
			return None
		else:
			
			if ( tmp.size < tmp2.size ) :
				tmp.parent = tmp2
				tmp2.size = tmp2.size + tmp.size
				return tmp
			else:
				tmp2.parent = tmp
				tmp2.size = tmp.size+ tmp2.size
				return tmp



def main():
	l = [ 1, 2, 34, 4, 5 ]
 	r = Initialize(l)
	print Find(r, 1)	
	print Find(r,2)
	print Find(r,5)
	for x in r :
		print x.name
	print Merge(r, 2, 34).name
	print Merge(r, 5, 34).name




if __name__ == "__main__" : main()
