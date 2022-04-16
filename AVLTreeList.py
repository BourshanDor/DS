# username - dorbourshan
# id1      - ***REMOVED***
# name1    - Dor Bourshan
# id2      - ***REMOVED***
# name2    - Jonathan Yahav

from printree import *

"""A class representing a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""

	def __init__(self, value):
		self.value = value
		if isinstance(self, AVLVirtualNode):
			self.left = None
			self.right = None
			self.height = -1
			self.size = 0

		else:
			self.left = AVLVirtualNode(self)
			self.right = AVLVirtualNode(self)
			self.height = 0
			self.size = 1
		self.parent = None

	"""printable representation of the AVLNode.
	"""
	def __repr__(self):
		return self.getValue() or "#"

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
	Complexity: O(1). The field is maintained based on direct descendents,
	like similar cases we saw in class.
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	
	"""
	def getHeight(self):
		return -1 if not self.isRealNode() else max(self.getRight().height, self.getLeft().height) + 1

	"""returns the size
	Complexity: O(1). The field is maintained based on direct descendents,
	like similar cases we saw in class.
	@rtype: int
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		return 0 if not self.isRealNode() else self.getLeft().size + self.getRight().size + 1

	"""return the balance factor of node, AVLTrees def that every node fulfill |BF(v)| <= 1 

	@rtype: int
	@:returns: The balance factor of the node
	"""
	def getBF(self):
		return self.getLeft().getHeight() - self.getRight().getHeight() if self.isRealNode() else 0

	""" 
	Sets input node as left child of self, and sets self as parent of input node.
	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		node.setParent(self)
		return None

	"""
	Sets input node as right child of self, and sets self as parent of input node.
	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		node.setParent(self)
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

	"""sets the height of the node

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
		return not isinstance(self, AVLVirtualNode)

	"""return the balance factor of node, AVLTrees def that every node fulfill |BF(v)| <= 1 

		@rtype: bool
		@returns: True iff |BF(v)| <= 1
		"""
	def validBF(self):
		return abs(self.getBF()) <= 1

	"""The successor of the node v is the item following v in the list. 
	Runtime: O(log(n))
	@rtype: AVLNode || None
	@returns: Reference to successor node of self, None if self is the max node
	"""
	def successor(self):
		return self.getPredecessorOrSuccessor(True)

	"""The predecessor of the node v is the item before v in the list. 
	Runtime: O(log(n)
	@rtype: AVLNode || None
	@returns: Reference to predecessor node of self, None if self is the min node
	"""
	def predecessor(self):
		return self.getPredecessorOrSuccessor(False)

	def getPredecessorOrSuccessor(self, getSuccessor):
		"""
		Since the logic for finding the predecessor and successor are totally symmetrical, we carry it out based on
		the boolean parameter getSuccessor, finding the successor if it is true and the predecessor if it is false.
		Runtime: O(log(n)). Queries on AVL trees are O(log(n)).
		@param getSuccessor: True if we want the successor, false if we want the predecessor
		@rtype: AVLNode || None
		"""
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

	def predicate(self, origin, getSuccessor):
		"""
		Checks logical condition that we use in getPredecessorOrSuccessor
		Runtime: O(1)
		@rtype: boolean
		"""
		return self is not None and \
			(getSuccessor and (self.getLeft() is not origin)) or \
			(not getSuccessor and (self.getRight() is not origin))

	def recalculate(self):
		"""
		Recalculates node's height and size, used after changes in tree.
		O(1) runtime complexity since both fields are calculated in constant time
		based only on direct children of the node.
		@return: 0 if height did not change, 1 if it did
		"""
		oldHeight = self.height
		newHeight = self.getHeight()
		self.setSize(self.getSize())
		self.setHeight(newHeight)
		if oldHeight == newHeight:
			return 0
		else:
			return 1

	def checkParentSide(self):
		"""
		Checks if node is to its parent's right or left
		@rtype int
		@returns 0 if no parent, 1 if right, -1 if left
		"""
		par = self.getParent()
		if par is None:
			return 0
		if par.getRight() is self:
			return 1
		return -1


class AVLVirtualNode(AVLNode):
	"""
	Extension of AVLNode class to easily and uniquely distinguish virtual nodes from real nodes.
	"""
	def __init__(self, par):
		super().__init__(None)
		self.parent = par


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# self.searchTree = AVLSearchTree()

	def __repr__(self):
		out = ""
		for row in printree(self.root, False):  # need printree.py file
			out = out + row + "\n"
		return out

	def append(self, val):
		return self.insert(self.length(), str(val))
	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return not isinstance(self.root, AVLNode)

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
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""
	def insert(self, i, val):
		rotationCounter = 0
		insertionNode = AVLNode(val)
		if self.empty() or isinstance(self.root, AVLVirtualNode):
			self.root = insertionNode
			return rotationCounter
		if i == 0:
			first = self.firstByReference()
			insertionNode.setParent(first)
			first.setLeft(insertionNode)
		else:
			# Fetch the node at index i. Take one step right, then go all the way left.
			descendingPointer = self.retrieveByIndex(i-1)
			descendingPointer = descendingPointer.getRight()
			while descendingPointer.isRealNode():
				descendingPointer = descendingPointer.getLeft()
			# node now points to the virtual node which we want to replace with our insertionNode.
			# All that's left to do is set its parent and place it to the proper side of its parent.
			where = descendingPointer.checkParentSide()
			insertionNode.setParent(descendingPointer.getParent())
			self.assignParentSide(insertionNode, where, allowRoot=False)

		# After inserting our node, we traverse the branch from it to up the root, balancing and recalculating fields.
		return self.balanceTree(insertionNode, rotationCounter)

	def balanceTree(self, ascendingPointer, balanceCount=0):
		"""
		Traverses the branch from node to root, rotating and balancing as required.
		Runtime: O(log(n)).
		@param balanceCount: The number of balance operations carried out before called
		@param ascendingPointer: position to start traversing upwards from
		@rtype: int
		@return: balance operations performed
		"""
		while ascendingPointer is not None and ascendingPointer.getParent() is not ascendingPointer:
			heightDiff = ascendingPointer.recalculate()
			rotationCount = self.balanceNode(ascendingPointer)
			increment = rotationCount if rotationCount > 0 else heightDiff
			balanceCount += increment
			ascendingPointer = ascendingPointer.getParent()
		return balanceCount

	def deleteLeaf(self, leaf):
		"""
		Deletes a leaf by disconnecting it from the tree and replacing it with a virtual node.
		Runtime: O(1)
		@param leaf: A reference to the leaf to be deleted.
		@rtype: None
		"""
		par = leaf.getParent()
		side = leaf.checkParentSide()
		if side == 0:
			self.root = None
			return
		if side == 1:
			par.setRight(AVLVirtualNode(par))
		else:
			par.setLeft(AVLVirtualNode(par))
		leaf.setParent(None)

	def bypassDelete(self, node):
		"""
		Deletes a node with only one child from the tree by bypassing it.
		Runtime: O(1)
		@param node: A reference to the node to be deleted.
		@rtype: None
		"""
		par = node.getParent()
		child = node.getRight() if node.getRight().isRealNode() else node.getLeft()
		side = node.checkParentSide()
		if side == 0:
			self.root = child
			child.setParent(par)
			return
		if side == 1:
			par.setRight(child)
		else:
			par.setLeft(child)
		node.setParent(None)
		node.setLeft(AVLVirtualNode(node))
		node.setRight(AVLVirtualNode(node))

	def successorDelete(self, node, balanceCounter):
		"""
		Deletes a node with two children by swapping it with its successor, then deleting the latter by reference.
		Runtime: O(log(n)) (time required to find the successor).
		@param node: A reference to the node to be deleted.
		@param balanceCounter: The number of balancing operations carried out before the function was called.
		@rtype: int
		@returns: The total number of balancing operations carried out after deletion is complete.
		"""
		nodeLeft = node.getLeft()
		nodeRight = node.getRight()
		nodeParent = node.getParent()

		successor = node.successor()
		successorLeft = successor.getLeft()
		successorRight = successor.getRight()
		successorParent = successor.getParent()

		nodeSide = node.checkParentSide()
		successorSide = successor.checkParentSide()
		if nodeSide == 0:
			self.root = successor
		elif nodeSide == 1:
			nodeParent.setRight(successor)
			if successorSide == 1:
				successorParent.setRight(node)
			elif successorSide == -1:
				successorParent.setLeft(node)
		else:
			nodeParent.setLeft(successor)
			if successorSide == 1:
				successorParent.setRight(node)
			elif successorSide == -1:
				successorParent.setLeft(node)

		successor.setLeft(nodeLeft)
		successor.setRight(nodeRight)
		successor.setParent(nodeParent)

		node.setLeft(successorLeft)
		node.setRight(successorRight)
		node.setParent(successorParent)
		if successor is nodeRight:
			node.setParent(successor)
			successor.setRight(node)
		node.recalculate()
		successor.recalculate()
		return self.deleteByReference(node, balanceCounter)

	def deleteByReference(self, node, balanceCounter):
		"""
		Given a reference to a node, deletes it using the deletion function corresponding to its number of children.
		@param node: A reference to the node to be deleted.
		@param balanceCounter: The number of balancing operations carried out before the function was called.
		@rtype: int
		@returns: The total number of balancing operations carried out after deletion is complete.
		"""
		plus = 0
		par = node.getParent()
		if node.getSize() == 1:
			self.deleteLeaf(node)
		elif not (node.getLeft().isRealNode() and node.getRight().isRealNode()):
			self.bypassDelete(node)
		else:
			plus = self.successorDelete(node, balanceCounter)

		return self.balanceTree(par, balanceCounter) + plus

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		rotationCounter = 0
		node = self.retrieveByIndex(i)
		return self.deleteByReference(node, rotationCounter)

	"""returns the value of the first item in the list
	Runtime: O(log(n))
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.firstByReference().getValue() if self.firstByReference() is not None else None

	"""
	Returns a reference to the first item in the list, or None if the list is empty.
	Runtime: O(log(n)) (queries on AVL trees run in O(log(n)) time)
	@rtype: AVLTreeNode || None
	"""
	def firstByReference(self):
		if self.empty() or isinstance(self.root, AVLVirtualNode):
			return None
		next_left = self.root.getLeft()
		while next_left.isRealNode():
			next_left = next_left.getLeft()
		return next_left.getParent()

	"""returns the value of the last item in the list
	Runtime: O(log(n))
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.lastByReference().getValue() if self.lastByReference() is not None else None

	"""
	Returns a reference to the last item in the list, or None if the list is empty.
	Runtime: O(log(n)) (queries on AVL trees run in O(log(n)) time)
	@rtype: AVLTreeNode || None
	"""
	def lastByReference(self):
		if self.empty() or isinstance(self.root, AVLVirtualNode):
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
		arr = []
		if self.empty():
			return arr
		i = self.firstByReference()
		last = self.lastByReference()
		while i is not last:
			arr.append(i.getValue())
			i = i.successor()
		arr.append(last.getValue())
		return arr

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return 0 if self.empty() else self.root.getSize()

	"""splits the list at the i'th index
	Runtime: O(log(n)), as we saw in class.
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	@see: joinTreeList
	"""
	def split(self, i):
		pivot = self.retrieveByIndex(i)
		leftTree, rightTree = AVLTreeList(), AVLTreeList()
		pivot.getLeft().isRealNode() and leftTree.setRoot(pivot.getLeft())
		# Make sure to detach the new roots from the old parents!
		leftTree.empty() or leftTree.getRoot().setParent(None)
		pivot.getRight().isRealNode() and rightTree.setRoot(pivot.getRight())
		# Detach from old parents
		rightTree.empty() or rightTree.getRoot().setParent(None)
		ascendingPointer = pivot
		leftJoin = []
		rightJoin = []
		while ascendingPointer is not self.root:
			parentSide = ascendingPointer.checkParentSide()
			par = ascendingPointer.getParent()
			siblingRoot = par.getLeft() if parentSide == 1 else par.getRight()
			siblingTree = AVLTreeList()
			siblingTree.setRoot(siblingRoot)
			# Detach from old parents
			siblingTree.getRoot() and siblingTree.getRoot().setParent(None)
			if parentSide == 1:
				leftJoin.append([siblingTree, par])
			else:
				rightJoin.append([siblingTree, par])

			ascendingPointer = ascendingPointer.getParent()

		joinTreeList(leftTree, leftJoin, True)
		joinTreeList(rightTree, rightJoin, False)
		return [leftTree, pivot.getValue(), rightTree]

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	@post: lst is mutated and should not be reused!
	"""
	def concat(self, lst):
		EMPTY_TREE_HEIGHT = -1
		selfHeight = self.root.getHeight() if not self.empty() else EMPTY_TREE_HEIGHT
		lstHeight = lst.root.getHeight() if not lst.empty() else EMPTY_TREE_HEIGHT
		heightDiff = abs(selfHeight - lstHeight)
		if self.empty():
			self.setRoot(lst.root)
			return heightDiff
		if lst.empty():
			return heightDiff
		x = self.lastByReference()
		self.delete(self.length()-1)
		join(self, lst, x)
		return heightDiff

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		index = 0
		currentNode = self.firstByReference()
		last = self.lastByReference()
		while currentNode is not last:
			if currentNode.getValue() == val:
				return index
			index += 1
			currentNode = currentNode.successor()
		if currentNode is not None and currentNode.getValue() == val:
				return index
		return -1

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):

		return self.root if not self.empty() else None

	def setRoot(self, newNode):
		self.root = newNode

	def retrieveByIndex(self, i):
		"""retrieve pointer to the node in the list at index i

		Complexity: O(log(n))
		@precondition: 0 <= i < self.length()
		@param i: The intended index in the list
		@rtype: AVLNode
		@return: pointer to the node in the list at index i
		"""
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

	def balanceNode(self, node):
		"""
		Rotates node to restore legal balance factor.
		Implicitly checks if rotation is required; if not, returns 0.
		@param node: The potentially invariant-violating node
		@rtype: int
		@return: Number of rotations performed to restore balance to node
		@postcondition: Subtree rooted at node is a legal AVL tree
		"""
		rotationsPerformed = 0
		selfBF = node.getBF()
		if abs(selfBF) <= 1:
			return rotationsPerformed
		rightBF, leftBF = node.getRight().getBF(), node.getLeft().getBF()
		if selfBF > 1:
			if leftBF < 0:
				self.rotateLeft(node.getLeft())
				rotationsPerformed += 1
			self.rotateRight(node)
			rotationsPerformed += 1
		if selfBF < -1:
			if rightBF > 0:
				self.rotateRight(node.getRight())
				rotationsPerformed += 1
			self.rotateLeft(node)
			rotationsPerformed += 1
		return rotationsPerformed

	def rotateRight(self, axisNode):
		"""
		Carries out a right-rotation (like we saw in class) around axisNode.
		Runtime: O(1). Touches a set number of nodes.
		@precondition: axisNode is in need of a right rotation.
		@postcondition: Tree is a legal AVL tree.
		@rtype: None
		"""
		toPoint = axisNode.checkParentSide()
		movingNode = axisNode.getLeft()
		movingRightSub = movingNode.getRight()
		axisParent = axisNode.getParent()
		axisNode.setLeft(movingRightSub)
		movingNode.setRight(axisNode)
		movingNode.setParent(axisParent)
		axisNode.setParent(movingNode)
		self.assignParentSide(movingNode, toPoint)
		axisNode.recalculate()
		movingNode.recalculate()

	def rotateLeft(self, axisNode):
		"""
		Carries out a left-rotation (like we saw in class) around axisNode.
		Runtime: O(1). Touches a set number of nodes.
		@precondition: axisNode is in need of a left rotation.
		@postcondition: Tree is a legal AVL tree.
		@rtype: None
		"""
		toPoint = axisNode.checkParentSide()
		movingNode = axisNode.getRight()
		movingLeftSub = movingNode.getLeft()
		axisParent = axisNode.getParent()
		axisNode.setRight(movingLeftSub)
		movingNode.setLeft(axisNode)
		movingNode.setParent(axisParent)
		axisNode.setParent(movingNode)
		self.assignParentSide(movingNode, toPoint)
		axisNode.recalculate()
		movingNode.recalculate()

	def assignParentSide(self, node, toPoint, allowRoot=True):
		"""
		Given a node and its side in relation to its parent, assigns the node to be the corresponding child of its parent.
		@param node: The node to assign as a child
		@param toPoint: The side of node with respect to its parent
		@param allowRoot: Optional parameter determining whether the node can be assigned as the root of the tree.
		@rtype: None
		"""
		if toPoint == 1:
			node.getParent().setRight(node)
		elif toPoint == -1:
			node.getParent().setLeft(node)
		else:
			if not allowRoot:
				raise RuntimeError
			self.setRoot(node)


'''
	def specialRotation(self, axisNode):
		toPoint = axisNode.checkParentSide()
		if toPoint == -1 :
			self.specialRotationRight(axisNode)
		elif toPoint == 1 :
			self.specialRotationLeft(axisNode)


	def specialRotationRight(self, axisNode):
		b = axisNode.getRight()  ##b


		zPar = self.getParent()
		axisNode.setRight(axisParent)
		self.setLeft(b)
		axisNode.setRight(self)
		axisNode.setParent(zPar)

		self.recalculate()
		axisNode.recalculate()
		axisNode.recalculate()
'''


def join(leftTree, rightTree, connectingNode):
	"""
	Given two AVLTreeLists and a connecting node, joins them using the algorithm we saw in class.
	Runtime: O(log(n)) (as we saw in class)
	@param leftTree: The left AVLTreeList we wish to join; corresponds to the tree with smaller keys we saw in class.
	@param rightTree: The right AVLTreeList we wish to join; corresponds to the tree with greater keys we saw in class.
	@param connectingNode: The node about which we attach the two trees; it is placed "between" them.
	@rtype: None
	"""
	if handleEmptyJoin(leftTree, rightTree, connectingNode):
		return
	leftIsTaller = leftTree.root.getHeight() >= rightTree.root.getHeight()
	shorter = rightTree if leftIsTaller else leftTree
	taller = leftTree if leftIsTaller else rightTree
	node = taller.root
	while node.getHeight() > shorter.root.getHeight():
		node = node.getRight() if leftIsTaller else node.getLeft()
	par = node.getParent()
	if leftIsTaller:
		connectingNode.setLeft(node)
		connectingNode.setRight(rightTree.root)
		connectingNode.setParent(par)
		if par is not None:
			par.setRight(connectingNode)
		else:
			taller.setRoot(connectingNode)
	else:
		connectingNode.setRight(node)
		connectingNode.setLeft(leftTree.root)
		connectingNode.setParent(par)

		if par is not None:
			par.setLeft(connectingNode)
		else:
			taller.setRoot(connectingNode)
			taller.getRoot().setParent(None)

	taller.balanceTree(connectingNode)
	# set what was the shorter tree to point to the joined tree to avoid bugs
	shorter.setRoot(taller.root)


def handleEmptyJoin(leftTree, rightTree, connectingNode):
	"""
	Handles edge cases that may be encountered when joining trees, namely cases that arise from one or both of the
	trees being empty.
	Runtime: O(1).
	@param leftTree: The left AVLTreeList to be joined.
	@param rightTree: The right AVLTreeList to be joined.
	@param connectingNode: The node to connect between the trees.
	@rtype: boolean
	@return: False iff neither tree is empty
	@note: If at least one of the trees is empty, this function carries out the required "empty join" operation.
	"""
	if leftTree.empty():
		if rightTree.empty():
			leftTree.setRoot(connectingNode)
			rightTree.setRoot(connectingNode)
			return True
		rightTree.insert(0, connectingNode.getValue())
		rightTree.balanceTree(rightTree.retrieveByIndex(0))
		leftTree.setRoot(rightTree.root)
		return True
	elif rightTree.empty():
		leftTree.insert(leftTree.length(), connectingNode.getValue())
		leftTree.balanceTree(leftTree.retrieveByIndex(leftTree.length()-1))
		rightTree.setRoot(leftTree.root)
		return True
	return False


def joinTreeList(originalTree, treesToJoin, isLeft):
	"""
	Auxiliary method for split.
	Given an original tree and a list of trees to join to it (and a side to join to),
	joins all the trees in the list to the original list, mutating the original until it is the final, joined tree.
	Runtime: O(log(n)), as part of the algorithm for split which we saw in class.
	@param originalTree: The tree from which we begin joining; the lowest one.
	@param treesToJoin: An array of trees to join to originalTree.
	@param isLeft: Boolean parameter to determine join direction
	@rtype: None
	@see: split
	"""
	# Every tree in the list is represented by a sublist of length 2.
	for treeSublist in treesToJoin:
		siblingTree, commonParent = treeSublist[0], treeSublist[1]
		if siblingTree.getRoot() is not None:
			siblingTree.getRoot().setParent(None)

		commonParent.setLeft(AVLVirtualNode(commonParent))
		commonParent.setRight(AVLVirtualNode(commonParent))
		commonParent.setParent(None)
		if isLeft:
			join(siblingTree, originalTree, commonParent)
		else:
			join(originalTree, siblingTree, commonParent)
