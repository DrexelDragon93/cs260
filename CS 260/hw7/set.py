#!/usr/bin/env python

class Node:
  def __init__(self, value, parent = None):
    self.value = value
    self.parent = parent

  def __repr__(self):
    return "(value = %s, parent = %s)" % (self.value, self.parent)

class MFSet:
  """
  Sets are represented by trees of Nodes. Name of set is the value
  stored in the root node.
  """

  def __init__(self, values):
    # For quick lookup, create a map of values to the Nodes
    # that contain them.
    self.node_map = dict(zip(
      values,
      map(Node, values)
    ))

    # keep track of set sizes, all initialized to 1
    self.set_sizes = dict(zip(
      values,
      [1] * len(values)
    ))

  def find(self, value):
    # check if we have a node with the given value
    if not value in self.node_map:
        return None

    # find the root of the tree, collecting nodes along the way for path
    # compression
    path = []
    node = self.node_map[value]
    while node.parent is not None:
      path.append(node)
      node = node.parent

    # compress path
    for n in path:
      n.parent = node

    # return name of the tree
    return node.value

  def merge(self, value1, value2):
    # if either value is not stored, nothing to do
    if not value1 in self.node_map or not value2 in self.node_map:
      return

    # find the roots
    node1 = self.node_map[value1]
    while node1.parent is not None:
      node1 = node1.parent
    node2 = self.node_map[value2]
    while node2.parent is not None:
      node2 = node2.parent

    # check if already same tree
    if node1 == node2:
      return

    # merge smaller into larger
    size1 = self.set_sizes[node1.value]
    size2 = self.set_sizes[node2.value]

    if size1 < size2:
      node1.parent = node2
      self.set_sizes[node2.value] = size1 + size2
      del self.set_sizes[node1.value]
    else:
      node2.parent = node1
      self.set_sizes[node1.value] = size1 + size2
      del self.set_sizes[node2.value]

def Initialize(Values):
  """
  return a new set system with one element per set.

  Values is a list of values for the sets
  """

  return MFSet(Values)

def Find(S, value):
  """
  Return the name of the set in which value lives. Do path compression.

  Exactly what you return isn't important, as long as Find(set, val1)
  and Find(set, val2) are equal if and only if val1 and val2 are in the same
  set.
  """

  return S.find(value)

def Merge(S, value1, value2):
  """
  Merge operation.  Make sure you parent the smaller set to the larger.
  """

  S.merge(value1, value2)

