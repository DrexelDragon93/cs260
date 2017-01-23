#!/usr/bin/python

class MFSet():
	def __init__(self, label, parent=None, name=None):
			self.label = label
			self.parent = parent
			self.size = 1
			self.name = name	
						
	def __str__( self ):
			return "(%s, %s)" % ( self.label, self.parent)
	
	def echo( self ):
			print self.__str__()


