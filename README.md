# AVL Tree List

This project is an implementation of the List Abstract Data Type (ADT) using an AVL Tree as the underlying data structure. The AVL Tree provides a balanced binary search tree that ensures O(log n) time complexity for all the operations on the List.

## Features

* `empty` : Check if the List is empty
* `retrieve` : Retrieve an element at a given position in the List
* `insert` : Insert an element into the List at a given position
* `delete` : Delete an element from the List at a given position
* `first` : Retrieve the first element in the List
* `last` : Retrieve the last element in the List
* `listToArray`: Convert the List to an array
* `length` : Get the length of the List
* `split` : Split the List into two separate Lists
* `concat` : Concatenate two Lists together
* `search` : Search for an element in the List

## Getting Started

### Prerequisites
* Python 3.x

### Installing
1. Clone the project repository from GitHub: `git clone https://github.com/BourshanDor/DS.git `


### Usage
1. Import the AVLTreeList class from the AVLTreeList.py file in your Python code.
2. Create a new AVLTreeList object.
3. Use the available methods to perform operations on the List.

Here's an example code snippet for using the AVLTreeList:
 ```
from avl_tree_list import AVLTreeList

# Declare a new AVLTreeList object
list = AVLTreeList()

# Insert elements into the List
list.insert(10)
list.insert(20)
list.insert(30)

# Delete an element from the List
list.delete(20)


# Get the first and last elements in the List
print("First element: ", list.first())
print("Last element: ", list.last())

# Convert the List to an array
arr = list.listToArray()
print("Array representation of List: ", arr)


```


## Authors
* Jonathan Yahav 
* Dor Bourshan




