import random
from AVLTreeList import *

def insertions(tr : AVLTreeList, n : int):
    total = 0
    for i in range(n):
        insertionIndex = random.randrange(0, i) if i > 0 else 0
        total += tr.insert(insertionIndex, str(i))
    return total

def deletions(tr: AVLTreeList, n: int):
    total = 0
    for i in range(n):
        deletionIndex = random.randrange(0, n-i)
        total += tr.delete(deletionIndex)
    return total

def insertionsAndDeletions(tr: AVLTreeList, n: int):
    total = 0
    half = n // 2
    for i in range(half):
        insertionIndex = random.randrange(0, i) if i > 0 else 0
        tr.insert(insertionIndex, str(i))
    for i in range(n // 2):
        index = random.randrange(0, half)
        if i % 2 == 0:
            total += tr.insert(index, str(i))
        else:
            total += tr.delete(index)
    return total

def q1a():
    print("TESTING INSERTIONS")
    for i in range(10):
        tr = AVLTreeList()
        n = 1000 * (2 ** (i+1))
        print("Iteration:", i+1, "balance count:", insertions(tr, n))

def q1b():
    print("TESTING DELETIONS")
    for i in range(10):
        tr = AVLTreeList()
        n = 1000 * (2 ** (i+1))
        insertions(tr, n)
        print("Iteration:", i+1, "balance count:", deletions(tr, n))

def q1c():
    print("TESTING ALTERNATING INSERTIONS & DELETIONS")
    for i in range(10):
        tr = AVLTreeList()
        n = 1000 * (2 ** (i+1))
        print("Iteration:", i+1, "balance count:", insertionsAndDeletions(tr, n))


def q2a():
    print("TESTING ")

q1a()
print("\n\n\n")
q1b()
print("\n\n\n")
q1c()