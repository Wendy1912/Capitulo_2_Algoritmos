# Implement binary search trees using Tree and Node classes
# Nodes contain a key and some data

from LinkStack import *

class BinarySearchTree(object):  # A binary search tree class

# To preserve node integrity, node keys and children links should
# not be accessible from the caller, so we make the entire
# Node class hidden, but leave its attributes public for ease
# of manipulating them in the Tree class

   class __Node(object):         # A node in a binary search tree
      def __init__(              # Constructor takes a key that is
            self,                # used to determine the position
            key,                 # inside the search tree,
            data,                # the data associated with the key
            left=None,           # and a left and right child node
            right=None,
            secondary_left=None):         # if known
         self.key  = key         # Copy parameters to instance
         self.data = data        # attributes of the object
         self.leftChild = left
         self.rightChild = right
         self.secondaryLeftChild = secondary_left

      def __str__(self):         # Represent a node as a string 
         return "{" + str(self.key) + ", " + str(self.data) + "}"

   def __init__(self):        # The tree organizes nodes by their
      self.__root = None      # keys.  Initially, it is empty.
   
   def isEmpty(self):         # Check for empty tree
      return self.__root is None

   def root(self):            # Get the data and key of the root node
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No root node in empty tree")
      return (                # Otherwise return root data and its key
         self.__root.data, self.__root.key)
      
   def __find(self, goal, shallow=False):
    # Find a node whose key matches goal, and its parent
    # If shallow is True, stop at the first node with a matching key
    current = self.__root
    parent = self
    last_node = None
    while current:
        if goal == current.key:
            if shallow:
                return current, parent
            last_node = current
        parent = current
        current = current.leftChild if goal < current.key else current.rightChild

    return last_node, parent


   def search(self, goal, deepest=True):
      node, p = self.__find(goal, deepest)
      if node:
         # Si se encontró un nodo, buscar hacia la izquierda para encontrar el nodo más superficial
         while node.leftChild and node.leftChild.key == goal:
               node = node.leftChild
         return node.data
      else:
         return None

   def insert(self, key, data):
        node, parent = self.__find(key, shallow=False)
        if node:
            new_node = self.__Node(key, data, secondary_left=node.leftChild)
            node.leftChild = new_node
            return True
        if parent is self:
            self.__root = self.__Node(key, data)
        elif key < parent.key:
            parent.leftChild = self.__Node(key, data)
        else:
            parent.rightChild = self.__Node(key, data)
        return True

   def inOrderTraverse(       # Visit all nodes of the tree in-order
         self, function=print): # and apply a function to each node
      self.__inOrderTraverse( # Call recursive version starting at
         self.__root, function=function) # root node

   def __inOrderTraverse(     # Visit a subtree in-order, recursively
         self, node, function): # The subtree's root is node
      if node:                # Check that this is real subtree
         self.__inOrderTraverse( # Traverse the left subtree
            node.leftChild, function)
         function(node)       # Visit this node
         self.__inOrderTraverse( # Traverse the right subtree
            node.rightChild, function)

   def traverse_rec(self,         # Traverse the tree recursively in
                traverseType="in"): # pre, in, or post order
      if traverseType in [    # Verify type is an accepted value and
            'pre', 'in', 'post']: # use generator to walk the tree 
         return self.__traverse(  # yielding (key, data) pairs
            self.__root, traverseType) # starting at root
      
      raise ValueError("Unknown traversal type: " + str(traverseType))

   def __traverse(self,       # Recursive generator to traverse
                  node,       # subtree rooted at node in pre, in, or
                  traverseType): # post order
      if node is None:        # If subtree is empty, 
         return               # traversal is done
      if traverseType == "pre": # For pre-order, yield the current
         yield (node.key, node.data) # node before all the others
      for childKey, childData in self.__traverse( # Recursively
            node.leftChild, traverseType): # traverse the left subtree
         yield (childKey, childData)       # yielding its nodes
      if traverseType == "in": # If in-order, now yield the current
         yield (node.key, node.data) # node
      for childKey, childData in self.__traverse( # Recursively
            node.rightChild, traverseType): # traverse right subtree
         yield (childKey, childData)        # yielding its nodes
      if traverseType == "post": # If post-order, yield the current
         yield (node.key, node.data) # node after all the others

   def traverse(self,         # Non-recursive generator to traverse
                traverseType='in'): # tree in pre, in, or post order
      if traverseType not in [ # Verify traversal type is an
            'pre', 'in', 'post']: # accepted value
         raise ValueError(
            "Unknown traversal type: " + str(traverseType))
      
      stack = Stack()         # Create a stack
      stack.push(self.__root) # Put root node in stack
      
      while not stack.isEmpty(): # While there is work in the stack
         item = stack.pop() # Get next item
         if isinstance(item, self.__Node): # If it's a tree node
            if traverseType == 'post': # For post-order, put it last
               stack.push((item.key, item.data))
            stack.push(item.rightChild) # Traverse right child
            if traverseType == 'in': # For pre-order, put item 2nd
               stack.push((item.key, item.data))
            stack.push(item.leftChild) # Traverse left child
            if traverseType == 'pre': # For pre-order, put item 1st
               stack.push((item.key, item.data))
         elif item:           # Every other non-None item is a
            yield item        # (key, value) pair to be yielded

   def minNode(self):         # Find and return node with minimum key
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No minimum node in empty tree")
      node = self.__root      # Start at root
      while node.leftChild:   # While node has a left child,
         node = node.leftChild # follow left child reference
      return (node.key, node.data) # return final node key and data

   def maxNode(self):         # Find and return node with maximum key
      if self.isEmpty():      # If the tree is empty, raise exception
         raise Exception("No maximum node in empty tree")
      node = self.__root      # Start at root
      while node.rightChild:  # While node has a right child,
         node = node.rightChild # follow right child reference
      return (node.data, node.key) # return final node data and key
         
   def levels(self):          # Count the levels in the tree
      return self.__levels(self.__root) # Count starting at root
   
   def __levels(self, node):  # Recursively count levels in subtree
      if node:                # If a node is provided, then level is 1
         return 1 + max(self.__levels(node.leftChild),  # more than
                        self.__levels(node.rightChild)) # max child
      else: return 0          # Empty subtree has no levels

   def nodes(self):           # Count the tree nodes, using iterator
      count = 0               # Assume an empty tree
      for key, data in self.traverse(): # Iterate over all keys in any
         count += 1           # order and increment count
      return count

   def nodes_rec(self):       # Count the tree nodes, recursively
      return self.__nodes(self.__root) # Count starting at root
   
   def __nodes(self, node):   # Recursively count nodes in subtree
      if node:                # If a node is provided, then sum the
         return (1 + self.__nodes(node.leftChild) +  # node with those
                 self.__nodes(node.rightChild))      # of its children
      else: return 0          # Empty subtree has no nodes

   def print(self,            # Print the tree sideways with 1 node
             indentBy=4):     # on each line and indenting each level
      self.__pTree(self.__root, # by some blanks.  Start at root node
                   "ROOT:   ", "", indentBy) # with no indent
       
   def __pTree(self,          # Recursively print a subtree, sideways 
               node,          # with the root node left justified
               nodeType,      # nodeType shows the relation to its
               indent,        # parent and the indent shows its level
               indentBy=4):   # Increase indent level for subtrees
      if node:                # Only print if there is a node
         self.__pTree(node.rightChild, "RIGHT:  ", # Print the right
                      indent + " " * indentBy, indentBy) # subtree
         print(indent + nodeType, node) # Print this node
         self.__pTree(node.leftChild,  "LEFT:   ", # Print the left
                      indent + " " * indentBy, indentBy) # subtree

   def delete(self, goal, shallow=False):
    # Delete a node whose key matches goal
    # If shallow is True, delete the shallowest node with a matching key
    node, parent = self.__find(goal, shallow)
    if node is not None:    # If node was found, 
        return self.__delete(parent, node)  # then perform deletion at node under the parent
    return None             # Else return None for no deletion


   def __delete(self, parent, node):
      # Delete the specified node in the tree, modifying the parent node/tree
      deleted = node.data     # Save the data that's to be deleted

      if node.leftChild:      # Determine number of subtrees
         if node.rightChild:  # If both subtrees exist,
               self.__promote_successor(node)  # Then promote successor to replace deleted node
         else:                # If no right child, move left child up
               if parent is self:  # If parent is the whole tree,
                  self.__root = node.leftChild  # update root
               elif parent.leftChild is node:  # If node is parent's left child, update left child link
                  parent.leftChild = node.leftChild
               else:              # Else update right child link
                  parent.rightChild = node.leftChild
      else:                   # No left child; so promote right child
         if parent is self:  # If parent is the whole tree,
               self.__root = node.rightChild  # update root
         elif parent.leftChild is node:  # If node is parent's left child, update left child link
               parent.leftChild = node.rightChild
         else:              # Else update right child link
               parent.rightChild = node.rightChild

      return deleted          # Return the deleted node's data

   def __promote_successor( # When deleting a node with both subtrees,
         self,              # find successor on the right subtree, put
                            # its data in this node, and delete the
         node):             # successor from the right subtree
      successor = node.rightChild # Start search for successor in
      parent = node         # right subtree and track its parent
      while successor.leftChild: # Descend left child links until
         parent = successor # no more left links, tracking parent
         successor = successor.leftChild
      node.key = successor.key    # Replace node to delete with
      node.data = successor.data  # successor's key and data
      self.__delete(parent, successor) # Remove successor node
