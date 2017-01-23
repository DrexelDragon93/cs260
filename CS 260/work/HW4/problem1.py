#!/usr/bin/python

import tree
import stack
from lexer import *


# Transverses Tree for prefix
def pre(t):

	tmp = []
	if t != None:
		tmp = tmp[0:] + [t.label]
		tmp.extend(pre(t.right))
		tmp.extend(pre(t.left
	return tmp

# Transverses Tree for infix
def inForm(t):
	tmp = []
	if t!= None:
		tmp.extend(inForm(t.right))
		tmp = tmp[0:] + [t.label ]
		tmp.extend(inForm(t.left))
	return tmp

# Transverses Tree for postfix
def post(t):
	tmp = [] 
	if t != None:
		tmp.extend(post(t.right))
		tmp.extend(post(t.left))
		tmp = tmp[0:] + [ t.label ]
	return tmp


# Prints out list for viewing purposes
def printList(tmpList, string):
	print string, ' '.join(tmpList)


# Evaluates the expression utalizing stacks and postfix notation
def evalExpression( tmpList ) :
	OPERATORS = [ '+' , '-', '*', '/' ]
	evalStack = stack.Stack()	

	for x in tmpList :
		if str.isdigit( x ) :
			evalStack.push(int(x))
		else:
			q = evalStack.pop()
			y = evalStack.pop()
			sol = 0
			if x == OPERATORS[0]:
				sol = y + q
			elif x == OPERATORS[1]:
				sol = y -q
			elif x == OPERATORS[2]:
				sol = y * q
			elif x == OPERATORS[3]:
				sol = y / q  
			evalStack.push(sol)
	return evalStack.pop()

# The defention for a prefix input to create a binary tree
def preTree():
	tempStack = stack.Stack()
	preStack = stack.Stack()
	tmplist = []

	token = get_next_token()
	while token:
		tempStack.push(token)
		token = get_next_token()
	while not tempStack.isEmpty():
		tmplist = tmplist[0:] + [tempStack.pop()]
	for x in tmplist:
		token = x
		if str.isdigit( token[0] ) :
			preStack.push(tree.Tree(token)	)
		else :
			left = preStack.pop()
			right = preStack.pop()
			preStack.push(tree.Tree(token, right, left))
			
	tmp =  preStack.pop()	
	return tmp

# The defention for a postfix input to create a binary tree
def  postTree():
		nstack = stack.Stack()
		token = get_next_token()
		while token:
			if str.isdigit( token[0] ) :
				node = tree.Tree(token)
				nstack.push( node )

			else:
				left = None
				right = None	
				if not nstack.isEmpty():
					left = nstack.pop()
				if not nstack.isEmpty():
					right = nstack.pop()
				node =  tree.Tree(token, left, right )
				nstack.push( node )
			token = get_next_token()
		if not nstack.isEmpty():
			tmp = nstack.pop()
			return tmp

# The efention for infix input to create binary tree
def infixTree():
	infixStack = stack.Stack()
	token = get_next_token()
	a = None
	b = None
	sign = None
	while token:
		if str.isdigit( token[0] ) :
			node = tree.Tree(token)
			infixStack.push(node)
		else :
			sign = token
			token = get_next_token()
			if str.isdigit( token[0] ):	
				infixStack.push(tree.Tree(token))
				a = infixStack.pop()
				b = infixStack.pop()

				node = tree.Tree(sign, a, b)
				infixStack.push(node)
	
		token = get_next_token()
	if not infixStack.isEmpty() :
		tmp = infixStack.pop()
		return tmp






# Default start of program
if __name__ == "__main__" : postTree()
