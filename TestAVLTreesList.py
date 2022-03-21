import unittest
from AVLTreeList import AVLNode


class TestAVLTreesList(unittest.TestCase):
    def test_isRealNode(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLNode(None)
        tree_node2 = AVLNode('a')
        self.assertEqual(tree_node1.isRealNode(), False)
        self.assertEqual(tree_node2.isRealNode(), True)


    def test_getHeight(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLNode(None)
        tree_node2 = AVLNode('a')
        self.assertEqual(tree_node1.getHeight(), -1)
        self.assertEqual(tree_node2.getHeight(), 0)


    def test_getSize(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLNode(None)
        tree_node2 = AVLNode('a')
        self.assertEqual(tree_node1.getSize(), 0)
        self.assertEqual(tree_node2.getSize(), 1)

    def test_getParent(self):
        #self.assertEqual(common, desirable)
        tree_node1 = AVLNode('a')
        tree_node2 = AVLNode('b')
        tree_node2.setParent(tree_node1)

        self.assertEqual(tree_node2.getParent(), tree_node1)









if __name__ == '__main__':

    unittest.main()
