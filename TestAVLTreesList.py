import unittest
from AVLTreeList import *
import random


class TestAVLTreesList(unittest.TestCase):

    def test_empty(self):

        list = AVLTreeList()
        self.assertEqual(list.empty(), True)
        list.insert(0,'a')
        self.assertEqual(list.empty(), False)
        list.delete(0)
        self.assertEqual(list.empty(), True)

    def test_retrieve(self):

        list = AVLTreeList()
        lst = []

        for i in range(100):
            lst.append(str(random.randint(0,1000000)))

        for i in range(100):
            list.insert(i, lst[i])

        for i in range(100):
            self.assertEqual(list.retrieve(i), lst[i])
            self.assertEqual(list.retrieve(i) is None, False)
            self.assertEqual(list.retrieve(i) == '-1', False)
        TheTragedyofCoriolanus = []
        with open('The Tragedy of Coriolanus.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    TheTragedyofCoriolanus.append(word)

        list2 = AVLTreeList()
        i = 0
        for st in TheTragedyofCoriolanus:
            list2.insert(i, st)
            i += 1

        i = 0
        for st in TheTragedyofCoriolanus:
            self.assertEqual(list2.retrieve(i), st)
            i += 1


    def test_insert(self):
        list = AVLTreeList()

        self.assertEqual(list.insert(list.length(), '3'), 0)
        self.assertEqual(list.insert(list.length(), '1'), 1)
        self.assertEqual(list.insert(1, '2'),3)

        list = AVLTreeList()
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'T', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                '18', '19', '20', '21', '22']

        for i in range(len(vals)):
            list.insert(i, vals[i])

        self.assertEqual(list.insert(10, '***'), 5)
        self.assertEqual(list.insert(11, 'Amir'), 3)
        self.assertEqual(list.insert(9, 'Natan'), 1)
        self.assertEqual(list.insert(12, 'Omri'), 5)
        self.assertEqual(list.insert(26, 'Dani'), 0)
        self.assertEqual(list.insert(25, 'Noam'), 1)


    def test_delete(self):

        list = AVLTreeList()

        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']

        for i in range(len(vals)):
            list.insert(i, vals[i])

        self.assertEqual(list.delete(0), 0)
        self.assertEqual(list.delete(1), 2)
        self.assertEqual(list.delete(1), 0)
        self.assertEqual(list.delete(0),2)
        self.assertEqual(list.delete(2),0)
        self.assertEqual(list.delete(3),0)
        self.assertEqual(list.delete(1),0)
        self.assertEqual(list.delete(0),1)
        self.assertEqual(list.delete(0),0)
        self.assertEqual(list.delete(0),0)
        self.assertEqual(list.delete(0), 0)

        for i in range(len(vals)):
            list.insert(i, vals[i])


        self.assertEqual(list.delete(3), 0)


    def test_first(self):

        list = AVLTreeList()
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']

        for i in range(len(vals)):
            list.insert(i, vals[i])

        for i in range(len(vals)):
            self.assertEqual(list.first(), vals[i])
            list.delete(0)


    def test_last(self):

        list = AVLTreeList()
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        for i in range(len(vals)):
            list.insert(i, vals[i])

        for i in range(len(vals)):
            self.assertEqual(list.last(), vals[len(vals) - (i + 1)])
            list.delete(list.length()-1)

    def test_listToArray(self):

        TheTragedyofCoriolanus = []
        with open('The Tragedy of Coriolanus.txt', 'r') as f:
            for line in f:
                for word in line.split():
                    TheTragedyofCoriolanus.append(word)

        list2 = AVLTreeList()
        i = 0
        for st in TheTragedyofCoriolanus:
            list2.insert(i, st)
            i += 1

        self.assertListEqual(list2.listToArray(),TheTragedyofCoriolanus )

        list = AVLTreeList()
        lst = []

        for i in range(100):
            val = str(random.randint(0, 1000000))
            j = 0
            if len(lst) != 0:
                j = random.randint(0,len(lst) - 1)
            lst.insert(j, val)
            list.insert(j, val)

        self.assertListEqual(list.listToArray(), lst)

    def test_length(self):

        list = AVLTreeList()

        for i in range(100):
            val = str(random.randint(0, 1000000))
            j = 0
            if i != 0:
                j = random.randint(0, i)
            list.insert(j, val)
        for i in range(100):
            self.assertEqual(list.length(),100 - i )
            j = 0
            if 100 - i != 0 :
                j = random.randint(0, 100 - (i+1))
            list.delete(j)

    #
    # def testSplitCrashes(self):
    #
    #     tr = AVLTreeList()
    #     tr.insert(0, "A")
    #     tr.insert(0, "0")
    #     tr.insert(1, "1")
    #     tr.insert(0, "2")
    #     tr.insert(2, "3")
    #     tr.insert(1, "4")
    #     tr.insert(0, "5")
    #     tr.insert(6, "6")
    #     tr.insert(1, "7")
    #     tr.insert(4, "8")
    #
    #     for j in range(9):
    #         index = random.randrange(0, tr.length())
    #         tr.insert(index, str(j))
    #         print("Iteration:", j, "inserted at index:", index)
    #     print(tr)
    #     print(tr.split(8))
    #
    #
    # #
    # def testLotsaSplitCrashes(self):
    #     for i in range(1000):
    #         print("Iteration:", i + 1)
    #         tr1 = AVLTreeList()
    #         tr2 = AVLTreeList()
    #     #    n = 1000 * (2 ** (i))
    #         n = 5000
    #         for i in range(n):
    #             insertionIndex = random.randrange(0, i) if i > 0 else 0
    #             tr1.insert(insertionIndex, str(i))
    #             tr2.insert(insertionIndex, str(i))
    #
    #         leftRoot = tr2.getRoot().getLeft()
    #         tr2Left = AVLTreeList()
    #         tr2Left.setRoot(leftRoot)
    #         leftNode = tr2Left.lastByReference()
    #         # print(tr1)
    #         l = tr1.split(random.randrange(0, tr1.length()))
    #         self.assertEqual(l[0].length() + l[2].length(), n - 1)
    #         k = tr2.split(tr2.length()//2)
    #         self.assertEqual(k[0].length() + k[2].length(), n - 1)
    #         join(tr1, tr2, AVLNode("Q"))

    def test_split(self):
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        list = AVLTreeList()

        for i in range(len(vals)):
            list.insert(i, vals[i])
        lst = list.split(0)
        self.assertListEqual(lst[0].listToArray(), [])
        self.assertEqual(lst[1], '0')
        self.assertEqual(lst[2].listToArray(), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

        tallerTree = AVLTreeList()
        tallerTree.insert(0, '0')
        tallerTree.insert(0, '1')
        tallerTree.insert(0, '2')
        tallerTree.insert(0, '21')

        # print(tallerTree)
        smallerTree = AVLTreeList()
        smallerTree.insert(0, '3')
        a = AVLNode('3')
        join(smallerTree, tallerTree, a)
        # print(smallerTree)

    def test_concat(self):
        # T1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        # T2 = ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
        T1 = []
        T2 = ['A']

        tr1 = AVLTreeList()
        tr2 = AVLTreeList()

        for i in range(len(T2)):
            tr2.insert(i, T2[i])

        for i in range(len(T1)):
            tr1.insert(i, T1[i])

        # print(tr1)
        # print(tr2)
        # print(tr1.concat(tr2))
        # print(tr1)
        # print(tr1.listToArray())




    def testSearch(self):
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'T', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                '19', '20', '21', '22']
        tr = AVLTreeList()
        for i in range(len(vals)):
            tr.insert(i, vals[i])
        # print(tr.search('T'))
#
#
#
#
#
#     def test_isRealNode(self):
#         #self.assertEqual(common, desirable)
#         #treeNode1 = AVLVirtualNode(5)
#         treeNode2 = AVLNode('a')
#         self.assertEqual(treeNode2.isRealNode(), True)
#         self.assertEqual(treeNode2.getLeft().isRealNode(), False)
#         self.assertEqual(treeNode2.getRight().isRealNode(), False)
#
#
#
#     def test_getHeight(self):
#         #self.assertEqual(common, desirable)
#         tree_node1 = AVLVirtualNode('6')
#         tree_node2 = AVLNode('a')
#         self.assertEqual(tree_node1.getHeight(), -1)
#         self.assertEqual(tree_node2.getHeight(), 0)
#
#
#     def test_getSize(self):
#         #self.assertEqual(common, desirable)
#         tree_node1 = AVLVirtualNode('5')
#         tree_node2 = AVLNode('a')
#         self.assertEqual(tree_node1.getSize(), 0)
#         self.assertEqual(tree_node2.getSize(), 1)
#
#     def test_getParent(self):
#         #self.assertEqual(common, desirable)
#         tree_node1 = AVLNode('a')
#         tree_node2 = AVLNode('b')
#         tree_node2.setParent(tree_node1)
#
#         self.assertEqual(tree_node2.getParent(), tree_node1)
#     #
#     def test_repr(self):
#         node = AVLNode('1')
#         node.setRight(AVLNode('2'))
#         node.setLeft(AVLNode('2'))
#         tr = AVLTreeList()
#         tr.root = node
#
#
#     def test_right_rotation(self):
#         B = AVLNode("B")
#         A = AVLNode("A")
#         R = AVLNode("R")
#         L = AVLNode("L")
#         R.setParent(B)
#         A.setParent(B)
#         L.setParent(A)
#         A.setLeft(L)
#         v = AVLNode("v")
#         L.setLeft(v)
#         v.setParent(L)
#         B.setLeft(A)
#         B.setRight(R)
#         K = AVLNode("K")
#         K.setParent(A)
#         A.setRight(K)
#         tr = AVLTreeList()
#         tr.root = B
#         #print(tr)
#
#         tr.rotateRight(B)
#
#         #print(tr)
#
#         pointer = v
#         print("####### IN ORDER ######")
#         while pointer:
#             print(pointer)
#             pointer = pointer.successor()
#         print(R.successor())
#
#         print("####### REVERSE ORDER ######")
#         pointer = R
#         while pointer:
#             print(pointer)
#             pointer = pointer.predecessor()
#         print(v.predecessor())
#
#         tr.rotateLeft(A)
#         #print(tr)
#
#     def test_delete(self):
#         rotations = []
#         tr = AVLTreeList()
#         for i in range(500):
#             tr.insert(tr.length()//2, str(i))
#         tr.listToArray()
#         for i in range(500):
#             rotations.append(tr.delete(tr.length()-1))
#         print(tr.listToArray())
#         self.assertEqual(tr.listToArray(), [])
#         self.assertIn(4, rotations)
#         #print(tr)
#
#     # def test_insert_ListTree(self):
#     #     lst = ['a','b','c','d','e','f','g','h','a','b','a','b','c','d','e','f']
#     #     tr = AVLTreeList()
#     #     for i in range(len(lst)):
#     #         tr.insert(i,lst[i])
#     #     print(tr)
#     #     print(tr.listToArray())
#     #     self.assertEqual(tr.listToArray(),lst)
#     #
#
#     #
#     # def testSplit(self):
#     #     vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
#     #     tr = AVLTreeList()
#     #     for i in range(len(vals)):
#     #         tr.insert(i, vals[i])
#     #     print(tr)
#     #     out = tr.split(10)
#     #     print(out[0].listToArray())
#     #     print(out[1])
#     #     print(out[2].listToArray())
#     #
#     #
#
#
#
#
#
#
#
#
#
# def checkBalanceFactor(AVLTr):
#
#     def recurtionCheckBalanceFactor(AVLNo):
#         if AVLNo.isRealNode():
#             return
#         recurtionCheckBalanceFactor(AVLNo.getLeft())
#         if not AVLNo.validBF():
#             print("Wrong")
#         recurtionCheckBalanceFactor(AVLNo.getRight())
#
#     a = recurtionCheckBalanceFactor(AVLTr.getRoot())
#     print('Ok')


if __name__ == '__main__':
    unittest.main()
