#!/usr/bin/python


# The class defintion of a stack

class Stack : 
	
	# Inital setup
  def __init__(self) : 
    self.items = [] 

	# Add to stack
  def push(self, item) : 
    self.items.append(item) 

	# Pull from stack
  def pop(self) : 
    return self.items.pop() 

	# See if stack is empty
  def isEmpty(self) : 
    return (self.items == []) 
