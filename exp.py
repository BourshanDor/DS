import random
from AVLTreeList import *

def insertions(tr : AVLTreeList, n : int):
    total = 0
    for i in range(n):
        insertionIndex = random.randrange(0, i) if i > 0 else 0
        total += tr.insert(insertionIndex, str(i))
    return total

def q1():
    for i in range(10):
        tr = AVLTreeList()
        n = 1000 * (2 ** (i+1))
        print("Iteration:", i+1, "balance count:", insertions(tr, n))
        print("\n###########################\n")

q1()