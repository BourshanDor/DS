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
		#return -1 if not self.isRealNode() else max(self.getRight().getHeight(), self.getLeft().getHeight()) + 1
		return -1 if not self.isRealNode() else max(self.getRight().height, self.getLeft().height) + 1

	"""returns the size
	
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


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		node.setParent(self)
		return None

	"""sets right child

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
		return not isinstance(self, AVLVirtualNode)

	"""return the balance factor of node, AVLTrees def that every node fulfill |BF(v)| <= 1 

		@rtype: bool
		@returns: True iff |BF(v)| <= 1
		"""
	def validBF(self):
		return abs(self.getBF()) <= 1

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
	@return: 0 if height did not change, 1 if it did
	"""
	def recalculate(self):
		oldHeight = self.height
		newHeight = self.getHeight()
		self.setSize(self.getSize())
		self.setHeight(newHeight)
		if oldHeight == newHeight:
			return 0
		else:
			return 1

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


class AVLVirtualNode(AVLNode):
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
		self.root = None; #TODO: change to correct init value
		# self.searchTree = AVLSearchTree()

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
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		rotationCounter = 0
		insertionNode = AVLNode(val)
		if self.empty():
			self.root = insertionNode
			return rotationCounter
		if i == 0:
			first = self.first()
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

	"""
	Traverses the branch from node to root, rotating and balancing as required.
	Runtime: O(logn).
	@param ascendingPointer: position to start traversing upwards from
	@rtype: int
	@returns: balance actions performed
	"""
	def balanceTree(self, ascendingPointer, balanceCount=0):
		while ascendingPointer is not None:
			heightDiff = ascendingPointer.recalculate()
			rotationCount = self.balanceNode(ascendingPointer)
			increment = rotationCount if rotationCount > 0 else heightDiff
			balanceCount += increment
			ascendingPointer = ascendingPointer.getParent()
		return balanceCount

	def deleteLeaf(self, leaf):
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

	def successorDelete(self, node, rotationCounter):
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
		#print(successor.getHeight())
		successor.recalculate()
		return self.deleteByReference(node, rotationCounter)

	def deleteByReference(self, node, rotationCounter):
		plus = 0
		par = node.getParent()
		if node.getSize() == 1:
			self.deleteLeaf(node)
		elif not (node.getLeft().isRealNode() and node.getRight().isRealNode()):
			self.bypassDelete(node)
		else:
			plus = self.successorDelete(node, rotationCounter)

		return self.balanceTree(par, rotationCounter) + plus

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
		arr = []
		if self.empty():
			return arr
		i = self.first()
		last = self.last()
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

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i, byReference=False):
		pivot = self.retrieveByIndex(i) if not byReference else i
		leftTree, rightTree = AVLTreeList(), AVLTreeList()
		leftTree.setRoot(pivot.getLeft())
		rightTree.setRoot(pivot.getRight())
		ascendingPointer = pivot
		leftJoin = []
		rightJoin = []
		while ascendingPointer is not self.root:
			parentSide = ascendingPointer.checkParentSide()
			par = ascendingPointer.getParent()
			siblingRoot = par.getLeft() if parentSide == 1 else par.getRight()
			siblingTree = AVLTreeList()
			siblingTree.setRoot(siblingRoot)
			if parentSide == 1:
				leftJoin.append([siblingTree, par])
			else:
				rightJoin.append([siblingTree, par])

			ascendingPointer = ascendingPointer.getParent()
		j1 = joinTreeList(leftTree, leftJoin, True)
		j2 = joinTreeList(rightTree, rightJoin, False)

		total = j1[0] + j2[0]
		count = j1[1] + j2[1]
		average = total / count
		maximum = max(j1[2], j2[2])
		return [average, maximum]
		#return [leftTree, pivot.getValue(), rightTree]


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
		x = self.last()
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
		currentNode = self.first()
		last = self.last()
		while currentNode is not last:
			if currentNode.getValue() == val:
				return index
			index += 1
			currentNode = currentNode.successor()
		return -1

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
				self.rotateLeft(node.getLeft())
				rotationsPerformed += 1
			if leftBF == 0:
				print("HEGATI LEPOHHHH")
				self.specialRotation(self.getLeft())
				return 0
			self.rotateRight(node)
			rotationsPerformed += 1
		if selfBF < -1:
			if rightBF > 0:
				self.rotateRight(node.getRight())
				rotationsPerformed += 1
			if rightBF == 0:
				print("HEGATI LEPOH GAM")
				return 0
			self.rotateLeft(node)
			rotationsPerformed += 1
		return rotationsPerformed

	""" 
	"""
	# TODO: Add docs
	def rotateRight(self, axisNode):
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

	"""
	"""
	# TODO: Add docs
	def rotateLeft(self, axisNode):
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

	"""
	"""
	# TODO: Add docs
	def assignParentSide(self, node, toPoint, allowRoot=True):
		if toPoint == 1:
			node.getParent().setRight(node)
		elif toPoint == -1:
			node.getParent().setLeft(node)
		else:
			if not allowRoot:
				raise RuntimeError
			self.setRoot(node)

	def specialRotation(self, axisNode):
		toPoint = axisNode.checkParentSide()
		if toPoint == -1:
			self.specialRotationRight(axisNode)
		elif toPoint == 1:
			self.specialRotationLeft(axisNode)

	def specialRotationRight(self, axisNode):
		b = axisNode.getRight()  ##b
		zPar = self.getParent()
		self.setLeft(b)
		axisNode.setRight(self)
		axisNode.setParent(zPar)

		self.recalculate()
		axisNode.recalculate()
		axisNode.recalculate()


def join(leftTree, rightTree, x):
	if handleEmptyJoin(leftTree, rightTree, x):
		return 0
	leftIsTaller = leftTree.root.getHeight() >= rightTree.root.getHeight()
	shorter = rightTree if leftIsTaller else leftTree
	taller = leftTree if leftIsTaller else rightTree
	heightDiff = abs(leftTree.root.getHeight() - rightTree.root.getHeight())
	node = taller.root
	while node.getHeight() > shorter.root.getHeight():
		node = node.getRight() if leftIsTaller else node.getLeft()
	par = node.getParent()
	if leftIsTaller:
		x.setLeft(node)
		x.setRight(rightTree.root)
		x.setParent(par)
		if par is not None:
			par.setRight(x)
		else:
			taller.setRoot(x)
	else:
		x.setRight(node)
		x.setLeft(leftTree.root)
		x.setParent(par)
		if par is not None:
			par.setLeft(x)
		else:
			taller.setRoot(x)

	taller.balanceTree(x)
	# set what was the shorter tree to point to the joined tree to avoid bugs
	shorter.setRoot(taller.root)
	return heightDiff

def handleEmptyJoin(leftTree, rightTree, x):
	if leftTree.empty():
		if rightTree.empty():
			leftTree.setRoot(x)
			rightTree.setRoot(x)
			return True
		rightTree.insert(0, x)
		leftTree.setRoot(rightTree.root)
		return True
	elif rightTree.empty():
		leftTree.insert(leftTree.length(), x)
		rightTree.setRoot(leftTree.root)
		return True
	return False

def joinTreeList(originalTree, treesToJoin, isLeft):
	total = 0
	count = 0
	maximum = 0
	j = 0
	for tup in treesToJoin:
		if tup[0].getRoot():
			tup[0].getRoot().setParent(None)
		tup[1].setLeft(AVLVirtualNode(tup[1]))
		tup[1].setRight(AVLVirtualNode(tup[1]))
		tup[1].setParent(None)
		if isLeft:
			j = join(tup[0], originalTree, tup[1])
		else:
			j = join(originalTree, tup[0], tup[1])
		total += j
		count += 1
		maximum = max(maximum, j)
	return [total, count, maximum]

