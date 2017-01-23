#!/usr/bin/env python

class BSTNode:
  def __init__( self, value, left = None, right = None ):
    self.value = value
    self.left = left
    self.right = right

  def __repr__( self ):
    return "(%s, %s, %s)" % ( self.value, self.left, self.right )

  def member( self, x ):
    if x == self.value:
      return True
    if x < self.value:
      if self.left is None:
        return False
      else:
        return self.left.member( x )
    elif x > self.value:
      if self.right is None:
        return False
      else:
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

  def delete( self, x ):
    if x < self.value:
      if self.left is not None:
        self.left.delete( x )
    elif x > self.value:
      if self.right is not None:
        self.right.delete( x )
    elif self.left is None:
      self = self.right
    elif self.right is None:
      self = self.left
    else:
      if self.right.left is None:
        self.value = self.right.value
        self.right = self.right.right
      else:
        self.value = self.right._deletemin()

  def _deletemin( self ):
    if self.left.left is None:
      minimum = self.left.value
      self.left = self.left.right
      return minimum
    else:
      return self.left._deletemin()

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

  values = [10, 5, 14, 14, 7, 12, 18, 15]
  
  tree = BST()
  for x in values:
    tree.insert( x )

  print tree # figure 5.1(a), pg. 156

  assert tree.member( 14 )
  assert not tree.member( 13 )

  tree.delete( 14 )
  assert not tree.member( 14 )
  tree.delete( 14 )
  print tree

if __name__ == "__main__":
  main()

