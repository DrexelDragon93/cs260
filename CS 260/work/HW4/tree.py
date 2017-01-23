#!/usr/bin/pyhton


#Class defition of tree
class Tree(object):

	# intital setup
	def __init__(self, label, left_child=None, right_child=None):
		self.label = label
		self.left = left_child
		self.right = right_child

	# print tree for debugging purpose
	def __str__( self ):
		return "(%s, %s, %s)" % ( self.label, self.left, self.right )
	
	# echo 
	def echo( self ):
		print self.__str__()


