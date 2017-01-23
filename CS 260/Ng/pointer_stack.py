#!/usr/bin/env python
from datetime import datetime
# STACK
# pointer implementation
class node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
		
	def __str__( self ):
		return "(%s, %s)" % ( self.data, self.next )
				
B = node(1,node(2,node(3,node(4,node(5,None)))))

def top(s):
	first = s.data
	return first
	
def pop(s):
	s = s.next
	return s
	
def push(s,x):
	temp = node(x,s)
	return temp

def empty(s):
	if s.data == None and s.next == None:
		return True
	else:
		return False

def makenull(s):
	while s.next != None:
		s = s.next
		s.data = None
	return s

# timing

B1= node(1,node(2,node(3,node(4,node(5,None)))))
B2= node(1,node(2,node(3,node(4,node(5,node(6,node(7,node(8,node(10,None)))))))))
B3= node(1,node(2,node(3,node(4,node(5,node(6,node(7,node(8,node(10,node(11,node(12,node(13,node(14,node(15,None))))))))))))))
	
def iter_pop(s):
	temp = s
	count = 0
	while s != None:
		s = s.next
		count = count + 1
	size = range(count - 1)
	for i in size:
		temp = pop(temp)
		print temp
		
def iter_push(s):
	temp = s
	count = 0
	while s != None:
		s = s.next
		count = count + 1
	size = range(count )
	for i in size:
		temp = push(temp,0)
		print temp
	
def main():
	# print iter_push(B1)
	# print top(B)
	# print pop(B)
	# print push(B,0)
	# print empty(B)
	# print makenull(B)
	
	# startTime = datetime.now()
	# iter_pop(B1)
	# iter_pop(B2)
	# iter_pop(B3)
	# iter_push(B1)
	# iter_push(B2)
	# iter_push(B3)
	# print datetime.now() - startTime
if __name__ == '__main__':main()