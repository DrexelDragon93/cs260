# tree functions

def tree_visit_pre( tree ):
  """
  Visit a tree represented by a tuple ( Value, Left, Right ) visiting
  the nodes preorder
  """

  if tree is None:
    return []

  order = []
  order.append( str( tree[0] ) )
  order.extend( tree_visit_pre( tree[1] ) )
  order.extend( tree_visit_pre( tree[2] ) )
  return order

def tree_visit_in( tree ):
  """
  Visit a tree represented by a tuple ( Value, Left, Right ) visiting
  the nodes inorder
  """

  if tree is None:
    return []

  order = []
  order.extend( tree_visit_in( tree[1] ) )
  order.append( str( tree[0] ) )
  order.extend( tree_visit_in( tree[2] ) )
  return order

def tree_visit_post( tree ):
  """
  Print a tree represented by a tuple ( Value, Left, Right ) visiting
  the nodes postorder
  """

  if tree is None:
    return []

  order = []
  order.extend( tree_visit_post( tree[1] ) )
  order.extend( tree_visit_post( tree[2] ) )
  order.append( str( tree[0] ) )
  return order

def tree_eval( tree ):
  """
  Evaluate a tree represented by a tuple ( Value, Left, Right ) where Value
  is either an integer (assume leaf node) or one of +-*/ (assume internal node
  with two children
  """

  if tree is None:
    return None

  value = tree[0]
  if isinstance( value, int ):
    return value

  left = tree_eval( tree[1] )
  right = tree_eval( tree[2] )

  if value == "+":
    return left + right
  elif value == "-":
    return left - right
  elif value == "*":
    return left * right
  elif value == "/":
    return left / right
  else:
    return None

