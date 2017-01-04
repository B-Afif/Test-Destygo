class Node:
  def __init__(self, val)
    self.left = None # is a Node
    self.right = None # is a Node
    self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
  def __init__(self, node)
    self.root = node
  
  def add(self):
    # TODO