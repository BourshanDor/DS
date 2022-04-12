import unittest
from AVLTreeList import *
import random



class TestAVLTreesList(unittest.TestCase):
    def test_isRealNode(self):
        #self.assertEqual(common, desirable)
        #treeNode1 = AVLVirtualNode(5)
        treeNode2 = AVLNode('a')
        self.assertEqual(treeNode2.isRealNode(), True)
        self.assertEqual(treeNode2.getLeft().isRealNode(), False)
        self.assertEqual(treeNode2.getRight().isRealNode(), False)



    def test_getHeight(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLVirtualNode('6')
        tree_node2 = AVLNode('a')
        self.assertEqual(tree_node1.getHeight(), -1)
        self.assertEqual(tree_node2.getHeight(), 0)


    def test_getSize(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLVirtualNode('5')
        tree_node2 = AVLNode('a')
        self.assertEqual(tree_node1.getSize(), 0)
        self.assertEqual(tree_node2.getSize(), 1)

    def test_getParent(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLNode('a')
        tree_node2 = AVLNode('b')
        tree_node2.setParent(tree_node1)

        self.assertEqual(tree_node2.getParent(), tree_node1)
    #
    # def test_repr(self):
    #     node = AVLNode('1')
    #     node.setRight(AVLNode('2'))
    #     node.setLeft(AVLNode('2'))
    #     tr = AVLTreeList()
    #     tr.root = node


    # def test_right_rotation(self):
    #     B = AVLNode("B")
    #     A = AVLNode("A")
    #     R = AVLNode("R")
    #     L = AVLNode("L")
    #     R.setParent(B)
    #     A.setParent(B)
    #     L.setParent(A)
    #     A.setLeft(L)
    #     v = AVLNode("v")
    #     L.setLeft(v)
    #     v.setParent(L)
    #     B.setLeft(A)
    #     B.setRight(R)
    #     K = AVLNode("K")
    #     K.setParent(A)
    #     A.setRight(K)
    #     tr = AVLTreeList()
    #     tr.root = B
    #     #print(tr)
    #
    #     tr.rotateRight(B)
    #
    #     #print(tr)
    #
    #     pointer = v
    #     print("####### IN ORDER ######")
    #     while pointer:
    #         print(pointer)
    #         pointer = pointer.successor()
    #     print(R.successor())
    #
    #     print("####### REVERSE ORDER ######")
    #     pointer = R
    #     while pointer:
    #         print(pointer)
    #         pointer = pointer.predecessor()
    #     print(v.predecessor())
    #
    #     tr.rotateLeft(A)
    #     #print(tr)
    #
    # def test_delete(self):
    #     rotations = []
    #     tr = AVLTreeList()
    #     for i in range(500):
    #         tr.insert(tr.length()//2, str(i))
    #     tr.listToArray()
    #     for i in range(501):
    #         rotations.append(tr.delete(tr.length()-1))
    #     print(tr.listToArray())
    #     self.assertEqual(tr.listToArray(), [])
    #     self.assertIn(4, rotations)
    #     #print(tr)
    #
    # def test_insert_ListTree(self):
    #     lst = ['a','b','c','d','e','f','g','h','a','b','a','b','c','d','e','f']
    #     tr = AVLTreeList()
    #     for i in range(len(lst)):
    #         tr.insert(i,lst[i])
    #     print(tr)
    #     print(tr.listToArray())
    #     self.assertEqual(tr.listToArray(),lst)

    # def test_concat(self):
    #     #T1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    #     #T2 = ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
    #     T1 = []
    #     T2 = ['A']
    #
    #     tr1 = AVLTreeList()
    #     tr2 = AVLTreeList()
    #
    #     for i in range(len(T2)):
    #         tr2.insert(i,T2[i])
    #
    #     for i in range(len(T1)):
    #         tr1.insert(i,T1[i])
    #
    #    # print(tr1)
    #     print(tr2)
    #     print(tr1.concat(tr2))
    #     print(tr1)
    #     print(tr1.listToArray())

    def testSplit(self):
        vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
        tr = AVLTreeList()
        for i in range(len(vals)):
            tr.insert(i, vals[i])
        print(tr)
        out = tr.split(10)
        print(out[0].listToArray())
        print(out[1])
        print(out[2].listToArray())

    # def test_insert_SearchTree(self):

        # lst = ['aa','a','b','c','d','aaa','e','f','g','h','tt']
        # tr = AVLSearchTree()
        # for i in range(len(lst)):
        #     tr.insert(lst[i],0)
        # print(tr)
        # print(tr.listToArray())
        # #self.assertEqual(tr.listToArray(),lst)










def checkBalanceFactor(AVLTr):

    def recurtionCheckBalanceFactor(AVLNo):
        if AVLNo.isRealNode():
            return
        recurtionCheckBalanceFactor(AVLNo.getLeft())
        if not AVLNo.validBF():
            print("Wrong")
        recurtionCheckBalanceFactor(AVLNo.getRight())

    recurtionCheckBalanceFactor(AVLTr.root())

if __name__ == '__main__':

    unittest.main()
