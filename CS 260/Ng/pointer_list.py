#!/usr/bin/env python
from datetime import datetime
# pointer implementation
#LIST
class node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
		
	def __str__( self ):
		return "(%s, %s)" % ( self.data, self.next )
				
A= node(1,node(2,node(3,node(4,node(5,None)))))

def first(l):
	return l.data

def end(l):
	i = 0
	while l.next != None:
		i = i + 1
		l = l.next		
	return i + 1

def retrieve(l,p):
	for i in range(0,p):
		l = l.next
	return l.data
	
def locate(l,x):
	pos = 0
	while l != None:
		if l.data == x:
			return pos
		l = l.next
		pos = pos + 1

def next(l,p):
	i = 0
	while l.next != None:
		i = i + 1
		l = l.next		
	if p >= i:
		return i
	else:
		return p + 1
	
def previous(l,p):
	if p - 1 <= 0:
		return 0
	else:
		return p - 1
	
def insert(l,p,x):
	temp1 = None
	for i in range(0,p+1):
		temp1 = node(l.data,temp1)
		l = l.next
	temp1 = node(x,temp1)
	while l != None:
		temp1 = node(l.data,temp1)
		l = l.next
	temp2 = None
	while temp1 != None:
		temp2 = node(temp1.data, temp2)
		temp1 = temp1.next
	return temp2

def delete(l,p):
	temp1 = None
	for i in range(0,p):
		temp1 = node(l.data,temp1)
		l = l.next
	l = l.next
	while l != None:
		temp1 = node(l.data,temp1)
		l = l.next
	temp2 = None
	while temp1 != None:
		temp2 = node(temp1.data, temp2)
		temp1 = temp1.next
	return temp2

def makenull(l):
	while l.next != None:
		l = l.next
		l.data = None
	return l




	
# timing

A1= node(1,node(2,node(3,node(4,node(5,None)))))
A2= node(1,node(2,node(3,node(4,node(5,node(6,node(7,node(8,node(10,None)))))))))
A3= node(1,node(2,node(3,node(4,node(5,node(6,node(7,node(8,node(10,node(11,node(12,node(13,node(14,node(15,None))))))))))))))

def front_insert(l):
	p = 0
	temp = l
	while l != None:
		print insert(temp,p,0)
		l = l.next
		p = p + 1		
			
def back_insert(l):
	p = 0
	temp = l
	while l != None:
		p = p + 1
		l = l.next
	size = range(p - 1,-1, -1)
	for i in size:
		print insert(temp,i,0)
		
def traverse(l):
	p = 0
	temp = l
	while p != end(temp) - 1:
		print l.data
		p = next(temp,p)
		l = l.next
	print l.data
		

def front_delete(l):
	p = 0
	temp = l
	while l != None:
		print delete(temp,p)
		l = l.next
		p = p + 1
		
def back_delete(l):
	p = 0
	temp = l
	while l != None:
		p = p + 1
		l = l.next
	size = range(p - 1,-1, -1)
	for i in size:
		print delete(temp,i)
		
def main():
	# print first(A)
	# print end(A)
	# print retrieve(A,1)
	# print locate(A, 2)
	# print next(A,2)
	# print previous(A,2)
	# print insert(A,2,0)
	# print delete(A, 2)
	# print makenull(A)
	
	# startTime = datetime.now()
	# front_insert(A1)
	# front_insert(A2)
	# front_insert(A3)
	# back_insert(A1)
	# back_insert(A2)
	# back_insert(A3)
	# traverse(A1)
	# traverse(A2)
	# traverse(A3)
	# front_delete(A1)
	# front_delete(A2)
	# front_delete(A3)
	# back_delete(A1)
	# back_delete(A2)
	# back_delete(A3)
	# print datetime.now() - startTime
if __name__ == '__main__':main()
