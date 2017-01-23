#!/usr/bin/env python

class BSTNode:
  def __init__( self, value, left = None, right = None ):
    self.value = value
    self.left = left
    self.right = right

  def __repr__( self ):
    return "(%s, %s, %s)" % ( self.value, self.left, self.right )

  def member( self, x ):

		if x is self.value:
			return self.value
		else:
			if x < self.value:
				if not self.left is None:
					return self.left.member( x )
			else:
				if not self.right is None:
					return self.right.member( x )
	
  def insert( self, x ):
    if x < self.value:
      if self.left is None:
        self.left = BSTNode( x )
      else:
        self.left.insert( x )
    elif x > self.value:
      if self.right is None:
        self.right = BSTNode( x )
      else:
        self.right.insert( x )

  def deleteMin( self ):

		if self.left == None:
			tmp = self.value
			self.value= None
			return tmp
		else:
		 	return self.left.deleteMin()
	


  def delete( self, x ):
		if x < self.value:
			 return self.left.delete(x)
		elif x > self.value:
			 return self.right.delete(x)
		
		elif (self.left ==None) and (self.right == None):
			self = None
		elif self.left == None:
			self = self.right
		elif self.right == None:
			self = self.left
		else:	
			self.value  =  self.right.deleteMin()

class BST:
  def __init__( self, root = None ):
    self.root = root

  def __repr__( self ):
    return "%s" % self.root

  def member( self, x ):
    if self.root is None:
      return False

    return self.root.member( x )

  def insert( self, x ):
    if self.root is None:
      self.root = BSTNode( x )
    else:
      self.root.insert( x )

  def delete( self, x ):
    if self.root is None:
      return
    else:
        self.root.delete( x )

def main():

  values = [10, 5, 14, 7, 12, 18, 15]
  tree = BST()
  for x in values:
    tree.insert( x )


  print tree # figure 5.1(a), pg. 156
  assert tree.member( 14 )
  assert not tree.member( 13 )

  tree.delete(14)
  assert not tree.member( 14 )
  print tree

if __name__ == "__main__":
  main()

