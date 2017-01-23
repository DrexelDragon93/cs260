#!/usr/bin/env python

from lexer import *
from tree import *
from collections import deque

def parse_pre( values ):

  next_value = values.popleft()
  if isinstance( next_value, int ):
    return ( next_value, None, None )

  left = parse_pre( values )
  right = parse_pre( values )
  return ( next_value, left, right )

def main():
  """
  Parse an expression tree in pre-order and display the tree in pre-,
  in-, and post-order forms as well as its evaluated value
  """

  while get_expression():
    values = []

    # walk the tokens
    t = get_next_token()
    while t:
      if str.isdigit( t[0] ) : # we have a (non-negative) number
        values.append( int(t) )
      else:
        values.append( t )
      t = get_next_token()

    tree = parse_pre( deque( values ) )

    print "pre: %s"  % " ".join( tree_visit_pre( tree ) )
    print "in: %s"   % " ".join( tree_visit_in( tree ) )
    print "post: %s" % " ".join( tree_visit_post( tree ) )
    print "eval: %s" % tree_eval( tree )
    print ""

if __name__ == "__main__":
  main()

