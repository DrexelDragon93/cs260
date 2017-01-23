#!/usr/bin/env python
from datetime import datetime

#LIST

list = [1, 2, 3, 5]

# array implementation
def first(l):
	return l[0]

def end(l):
	last = len(l)
	return last

def retrieve(l,p):
	return l[p]

def locate(l,x):
	end = len(l) - 1
	for i in range(0, end + 1):
		if l[i] == x:
			return i
		elif (i == end):
			return end
		
def next(l,p):
	last = len(l) - 1
	if p >= last:
		return last
	else:
		return p + 1
		
def previous(l,p):
	if p - 1 <= 0:
		return 0
	else:
		return p - 1

def insert(l,p,x):
	array1 = l[0:p]
	array2 = l[p:]
	array1.append(x)
	return array1 + array2
	
def delete(l,p):
	array1 = l[:p]
	array2 = l[p + 1:]
	return array1 + array2
	
def makenull(l):
	l=[]
	return l

# tests

# print first(list)
# print end(list)
# print retrieve(list,1)
# print locate(list, 2)
# print next(list,2)
# print previous(list,2)
# print insert(list,2,0)
# print delete(list, 2)
# print makenull(list)

# timing

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
list3 = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15]

def front_insert(l):
	size = range(len(l) + 1)
	for i in size:
		print insert(l,i,0)
			
def back_insert(l):
	size = range(len(l),-1, -1)
	for i in size:
		print insert(l,i,0)
		
def traverse(l):
	p = 0
	while p != end(l) - 1:
		print l[p]
		p = next(l,p)
	print l[p]

def front_delete(l):
	size = range(len(l))
	for i in size:
		print delete(l,i)
			
def back_delete(l):
	size = range(len(l) - 1,-1, -1)
	for i in size:
		print delete(l,i)

	
# startTime = datetime.now()
# front_insert(list1)
# front_insert(list2)
# front_insert(list3)
# back_insert(list1)
# back_insert(list2)
# back_insert(list3)
# traverse(list1)
# traverse(list2)
# traverse(list3)
# front_delete(list1)
# front_delete(list2)
# front_delete(list3)
# back_delete(list1)
# back_delete(list2)
# back_delete(list3)
# print datetime.now() - startTime