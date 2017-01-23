#!/usr/bin/env python

from lexer import *
from tree import *

def main():
  """
  Parse an expression tree in post-order and display the tree in pre-,
  in-, and post-order forms as well as its evaluated value
  """

  while get_expression():
    # for each expression, start with an empty stack
    stack = []

    # walk the tokens
    t = get_next_token()
    while t:
      if str.isdigit( t[0] ) : # we have a (non-negative) number
        # add node to stack
        node = ( int(t), None, None )
        stack.append( node )
      else:
        # merge trees
        right = stack.pop()
        left = stack.pop()
        stack.append( ( t, left, right ) )
      t = get_next_token()

    tree = stack.pop()
    print "pre: %s"  % " ".join( tree_visit_pre( tree ) )
    print "in: %s"   % " ".join( tree_visit_in( tree ) )
    print "post: %s" % " ".join( tree_visit_post( tree ) )
    print "eval: %s" % tree_eval( tree )
    print ""

if __name__ == "__main__":
  main()

