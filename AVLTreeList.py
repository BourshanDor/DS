#username - dorbourshan
#id1      - ***REMOVED***
#name1    - Dor Bourshan
#id2      - ***REMOVED***
#name2    - Jonathan Yahav

from printree import *

"""A class represnting a node in an AVL tree"""

class AVLNode(object) :
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	@property
	def NO_STRING(self):
		return -1

	def __init__(self, value):
		self.value = value
		self.left = None if value == AVLNode.NO_STRING else AVLNode(AVLNode.NO_STRING)
		self.right = None if value == AVLNode.NO_STRING else AVLNode(AVLNode.NO_STRING)
		self.parent = None
		self.height = -1 if value == AVLNode.NO_STRING else 0
		self.size = 0 if value == AVLNode.NO_STRING else 1


	"""printable representation of the AVLNode.
	"""
	def __repr__(self):
		return self.getValue()


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	
	"""

	# TODO: Remember to update in insert function
	def getHeight(self):
		return -1 if not self.isRealNode() else max(self.getRight().getHeight(), self.getLeft().getHeight()) + 1

	"""returns the size
	
	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return 0 if not self.isRealNode() else self.left.getSize() + self.right.getSize() + 1

	"""return the balance factor of node, AVLTrees def that every node fulfill |BF(v)| <= 1 

	@rtype: int
	@:returns: The balance factor of the node
	"""
	def getBF(self):
		return self.getLeft().getHeight() - self.getRight().getHeight()


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		AVLNode.setParent(node, self)
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		AVLNode.setParent(node, self)
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		return None

	"""sets the size of the node
	@type s: int
	@param: the size
	"""
	def setSize(self, s):
		self.size = s
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False iff self is a virtual node.
	"""
	def isRealNode(self):
		return not (self.value == AVLNode.NO_STRING and self.getLeft() is None and self.getRight() is None)

	"""return the balance factor of node, AVLTrees def that every node fulfill |BF(v)| <= 1 

		@rtype: bool
		@returns: True iff |BF(v)| <= 1
		"""
	def validBF(self):
		return True if abs(self.getBF()) <= 1 else False

	"""The successor of the node v is the item following v in the list. 
	
	@rtype: AVLNode || None
	"""
	def successor(self):
		return self.getPredecessorOrSuccessor(True)

	"""The predecessor of the node v is the item before v in the list. 
	
	@rtype: AVLNode || None
	"""
	def predecessor(self):
		return self.getPredecessorOrSuccessor(False)

	"""
	Add docs
	"""
	def getPredecessorOrSuccessor(self, getSuccessor):
		v = self
		child = self.getRight() if getSuccessor else self.getLeft()
		par = self.getParent()

		if child.isRealNode():
			while child.isRealNode():
				v = child
				child = child.getLeft() if getSuccessor else child.getRight()
			return v

		while par is not None and par.predicate(v, getSuccessor):
			v = par
			par = par.getParent()
		return par

	"""
	"""
	# TODO: Add docs
	def predicate(self, origin, getSuccessor):
		return self is not None and \
				(getSuccessor and (self.getLeft() is not origin)) or \
				(not getSuccessor and (self.getRight() is not origin))

	"""
	Recalculates node's height and size, used after changes in tree.
	O(1) runtime complexity since both fields are calculated in constant time
	based only on direct children of the node.
	"""
	def recalculate(self):
		self.setSize(self.getSize())
		self.setHeight(self.getHeight())

	"""
	Checks if node is to its parent's right or left
	@rtype int
	@returns 0 if no parent, 1 if right, -1 if left
	"""
	def checkParentSide(self):
		par = self.getParent()
		if par is None:
			return 0
		if par.getRight() is self:
			return 1
		return -1



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = AVLNode(None); #TODO: change to correct init value
		# add your fields here

	def __repr__(self):
		out = ""
		for row in printree(self.root, False):  # need printree.py file
			out = out + row + "\n"
		return out

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise 
	"""
	def empty(self):
		return not self.root.isRealNode()

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return self.retrieveByIndex(i).getValue()


	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		return -1

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.empty():
			return None
		next_left = self.root.getLeft()
		while next_left.isRealNode():
			next_left = next_left.getLeft()
		return next_left.getParent()

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.empty():
			return None
		next_right = self.root.getRight()
		while next_right.isRealNode():
			next_right = next_right.getRight()
		return next_right.getParent()

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.root.getSize()

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		# TODO: look at Tree-Select in lecture 4 PowerPoint
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		# Idea: maintain a standard AVL tree
		# with the values of the list-tree as keys
		# and with pointers to the list nodes as values.
		# TODO: Implement (forum says this is allowed)
		return None

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root if self.root.isRealNode() else None

	def setRoot(self, newNode):
		self.root = newNode

	"""retrieve pointer to the node in the list at index i 
	
	Complexity: O(log(n))
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list 
	@rtype: AVLNode
	@return: pointer to the node in the list at index i 
	"""
	def retrieveByIndex(self, i):
		j = i + 1
		explore = self.root
		counter = explore.getLeft().getSize() + 1

		while j != counter:
			if j < counter:
				explore = explore.getLeft()
				counter = explore.getLeft().getSize() + 1

			else:
				j = j - counter
				explore = explore.getRight()
				counter = explore.getLeft().getSize() + 1

		return explore

	"""
	Rotates node to restore legal balance factor.
	Implicitly checks if rotation is required; if not, returns 0.
	@param node: The potentially invariant-violating node
	@rtype: int
	@returns: Number of rotations performed to restore balance to node
	@post: Subtree rooted at node is a legal AVL tree
	"""
	def balanceNode(self, node):
		rotationsPerformed = 0
		# FIXME: complexity?!
		selfBF = node.getBF()
		if abs(selfBF) <= 1:
			return rotationsPerformed
		rightBF, leftBF = node.getRight().getBF(), node.getLeft().getBF()
		if selfBF > 1:
			if leftBF < 0:
				self.rotateRight(node.getRight())
			self.rotateLeft(node)
			rotationsPerformed = 1
		if selfBF < -1:
			if rightBF > 0:
				self.rotateLeft(node.getLeft())
			self.rotateRight(node)
			rotationsPerformed = 1
		return rotationsPerformed

	""" 
	"""
	# TODO: Add docs
	def rotateRight(self, B):
		toPoint = B.checkParentSide()
		A = B.getLeft()
		A_r = A.getRight()
		BParent = B.getParent()

		B.setLeft(A_r)
		# A.setParent(B) // unless I'm missing something, we don't need this(?)
		A.setRight(B)
		A.setParent(BParent)
		B.setParent(A)
		self.assignParentSide(A, toPoint)
		B.recalculate()
		A.recalculate()

	"""
	"""
	# TODO: Add docs
	def rotateLeft(self, B):
		toPoint = B.checkParentSide()
		A = B.getRight()
		A_l = A.getLeft()
		BParent = B.getParent()

		B.setRight(A_l)
		A.setLeft(B)
		A.setParent(BParent)
		B.setParent(A)
		self.assignParentSide(A, toPoint)
		B.recalculate()
		A.recalculate()

	"""
	"""
	# TODO: Add docs
	def assignParentSide(self, A, toPoint):
		if toPoint == 1:
			A.getParent().setRight(A)
		elif toPoint == -1:
			A.getParent().setLeft(A)
		else:
			self.setRoot(A)
