import unittest
from AVLTreeList import *
import random



class TestAVLTreesList(unittest.TestCase):
    # def test_isRealNode(self):
    #     #self.assertEqual(common, desirable)
    #     tree_node1 = AVLVirtualNode()
    #     tree_node2 = AVLNode('a')
    #     self.assertEqual(tree_node1.isRealNode(), False)
    #     self.assertEqual(tree_node2.isRealNode(), True)
    #
    #
    # def test_getHeight(self):
    #     #self.assertEqual(common, desirable)
    #     tree_node1 = AVLVirtualNode()
    #     tree_node2 = AVLNode('a')
    #     self.assertEqual(tree_node1.getHeight(), -1)
    #     self.assertEqual(tree_node2.getHeight(), 0)
    #
    #
    # def test_getSize(self):
    #     #self.assertEqual(common, desirable)
    #     tree_node1 = AVLVirtualNode()
    #     tree_node2 = AVLNode('a')
    #     self.assertEqual(tree_node1.getSize(), 0)
    #     self.assertEqual(tree_node2.getSize(), 1)
    #
    # def test_getParent(self):
    #     #self.assertEqual(common, desirable)
    #     tree_node1 = AVLNode('a')
    #     tree_node2 = AVLNode('b')
    #     tree_node2.setParent(tree_node1)
    #
    #     self.assertEqual(tree_node2.getParent(), tree_node1)
    #
    # def test_repr(self):
    #     node = AVLNode('1')
    #     node.setRight(AVLNode('2'))
    #     node.setLeft(AVLNode('2'))
    #     tr = AVLTreeList()
    #     tr.root = node
    #
    #
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

    def test_insert(self):
        tr = AVLTreeList()



        for i in range (10):
            print(tr.insert(0,str(i)))
            print(tr)
        for i in range(5):
            tr.insert(2*(i+1), str(10*(i+1)))

        #for i in range(6):
         #   tr.insert(tr.length()//2,str(i+10))
        #print((tr.insert(tr.length()//2, "DOUBLE")))
        #print(tr.insert(0, "A"))
        #print(tr.insert(9,str(-1)))
        #print(tr.insert(11, str(-2)))
        #tr.insert(0,str(-2))


        print(tr)
        print(tr.listToArray())






if __name__ == '__main__':

    unittest.main()
