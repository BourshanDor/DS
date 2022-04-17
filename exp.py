import random
from AVLTreeList import *

RANDOM = 0
ORDERED = 1
SPECIAL = 2


def insertions(tr : AVLTreeList, n : int, doRotate=True, mode=RANDOM):
    total = 0
    depthTotal = 0
    for i in range(n):
        if mode == RANDOM:
            insertionIndex = (random.randrange(0, i) if i > 0 else 0)
        elif mode == ORDERED:
            insertionIndex = 0
        balanceOps, depth = tr.insert(insertionIndex, str(i), doRotate)
        total += balanceOps
        depthTotal += depth
    balanceAvg = total / n
    depthAvg = depthTotal / n
    return [balanceAvg, depthAvg]


def specialInsertions(tr : AVLTreeList, n: int, doRotate=True, mode=SPECIAL):
    total = 0
    depthTotal = 0
    amountInStep = 1
    numbersSoFar = 0

    while numbersSoFar < n :
        for num in range(amountInStep):
            if numbersSoFar >= n:
                break
            numbersSoFar += 1
            insertionIndex = num * 2
           # print(insertionIndex)
            balanceOps, depth = tr.insert(insertionIndex, str(numbersSoFar), doRotate)
            #print(tr)
            total += balanceOps
            depthTotal += depth
        amountInStep *= 2
    balanceAvg = total / n
    depthAvg = depthTotal / n
    return [balanceAvg, depthAvg]

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


question3_n = 1000


def q3a():
    print("TESTING UNBALANCED, ORDERED INSERTIONS")
    for i in range(10):
        n = question3_n * (i+1)
        balanced = AVLTreeList()
        unbalanced = AVLTreeList()
        balancedOpsAvg, balancedDepthAvg = insertions(balanced, n, True, ORDERED)
        unbalancedOpsAvg, unbalancedDepthAvg = insertions(unbalanced, n, False, ORDERED)
        print("Iteration:", i + 1)
        print("Average OPS in BALANCED tree:", balancedOpsAvg)
        print("Average DEPTH in BALANCED tree:", balancedDepthAvg)
        print("\n")
        print("Average OPS in UNBALANCED tree:", unbalancedOpsAvg)
        print("Average DEPTH in UNBALANCED tree:", unbalancedDepthAvg)
        print("\n\n")

def q3b():
    print("TESTING UNBALANCED, 'PERFECT SEQUENCE' INSERTIONS")
    print("Ops: balanced, unbalanced")
    print("Depths: balanced, unbalanced")
    for i in range(10):
        n = question3_n * (i + 1)
        balanced = AVLTreeList()
        unbalanced = AVLTreeList()
        balancedOpsAvg, balancedDepthAvg = specialInsertions(balanced, n, True, SPECIAL)
        unbalancedOpsAvg, unbalancedDepthAvg = specialInsertions(unbalanced, n, False, SPECIAL)
        print("Iteration:", i + 1)
        print(balancedOpsAvg, unbalancedOpsAvg)
        print("\n")
        print(balancedDepthAvg, unbalancedDepthAvg)
        print("\n\n")


def newRandomInsertions(balanced : AVLTreeList, unbalanced : AVLTreeList, n : int):
    balancedTotal = 0
    balancedDepthTotal = 0
    unbalancedTotal = 0
    unbalancedDepthTotal = 0
    for i in range(n):
        insertionIndex = (random.randrange(0, i) if i > 0 else 0)
        balTotInc, balDepInc = balanced.insert(insertionIndex, str(i), True)
        unbalTotInc, unbalDepInc = unbalanced.insert(insertionIndex, str(i), False)
        balancedTotal += balTotInc
        balancedDepthTotal += balDepInc
        unbalancedTotal += unbalTotInc
        unbalancedDepthTotal += unbalDepInc
    ret = [(balancedTotal / n), (unbalancedTotal / n), (balancedDepthTotal / n), (unbalancedDepthTotal / n)]
    return ret

def q3c():
    print("TESTING UNBALANCED, RANDOM INSERTIONS")
    balancedOps = []
    unbalancedOps = []
    balancedHeight = []
    unbalancedHeight = []
    for i in range(10):
        n = question3_n * (i + 1)
        balanced = AVLTreeList()
        unbalanced = AVLTreeList()
        retVal = newRandomInsertions(balanced, unbalanced, n)
        balancedOpsAvg, unbalancedOpsAvg = retVal[0], retVal[1]
        balancedDepthAvg, unbalancedDepthAvg = retVal[2], retVal[3]
        print("Iteration:", i + 1)
        print(unbalancedOpsAvg, balancedOpsAvg)
        print("\n")
        print(unbalancedDepthAvg, balancedDepthAvg)
        print("\n\n")


q3b()
