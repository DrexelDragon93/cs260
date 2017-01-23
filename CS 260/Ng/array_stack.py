#!/usr/bin/env python
from datetime import datetime

stack = [1, 2, 3, 5]
# STACK
# array implementation
def top(s):
	first = s[0]
	return first

def pop(s):
	return s[1:]
	
def push(s,x):
	temp = [x]
	return temp + s
	
def empty(s):
	if s == []:
		return True
	else:
		return False
	
def makenull(s):
	s = []
	return s

# tests

# print top(stack)
# print pop(stack)
# print push(stack,0)
# print empty(stack)
# print makenull(stack)

# timing
stack1 = [1, 2, 3, 4, 5]
stack2 = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
stack3 = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10, 11, 12, 13, 14, 15]

def iter_pop(s):
	size = range(len(s))
	for i in size:
		s = pop(s)
		print s
		
def iter_push(s):
	size = range(len(s))
	for i in size:
		s = push(s,0)
		print s
		
# startTime = datetime.now()
# iter_pop(stack1)
# iter_pop(stack2)
# iter_pop(stack3)
# iter_push(stack1)
# iter_push(stack2)
# iter_push(stack3)
# print datetime.now() - startTime