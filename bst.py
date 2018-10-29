"""
File: bst.py
BST class for binary search trees.
"""

from queue import LinkedQueue
from binarytree import BinaryTree

class BST(object):

    def __init__(self):
        self._tree = BinaryTree.THE_EMPTY_TREE
        self._size = 0


    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._tree)

    def __iter__(self):
        return iter(self.inorder())

    def find(self, target):
        """Returns data if target is found or None otherwise."""
        # Modified to set a couple data attributes: self._foundNode and
        # self._foundNodeParent
        def findHelper(tree):
            if tree.isEmpty():
                return None
            elif target == tree.getRoot():
                self._foundNode = tree
                return tree.getRoot()
            elif target < tree.getRoot():
                self._foundNodeParent = tree
                return findHelper(tree.getLeft())
            else:
                self._foundNodeParent = tree
                return findHelper(tree.getRight())

        self._foundNodeParent = None  # root node has no parent    
        return findHelper(self._tree)

    def add(self, newItem):
        """Adds newItem to the tree."""

        # Helper function to search for item's position 
        def addHelper(tree):
            currentItem = tree.getRoot()
            left = tree.getLeft()
            right = tree.getRight()

            # New item is less, go left until spot is found
            if newItem < currentItem:
                if left.isEmpty():
                    tree.setLeft(BinaryTree(newItem))
                else:
                    addHelper(left)                    

            # New item is greater or equal, 
            # go right until spot is found
            elif right.isEmpty():
                tree.setRight(BinaryTree(newItem))
            else:
                addHelper(right)
            # End of addHelper

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTree(newItem)

        # Otherwise, search for the item's spot
        else:
            addHelper(self._tree)
        self._size += 1

    def inorder(self):
        """Returns a list containing the results of
        an inorder traversal."""
        lyst = []
        self._tree.inorder(lyst)
        return lyst


    def preorder(self):
        """Returns a list containing the results of
        a preorder traversal."""
        # Exercise
        lyst = []
        self._tree.preorder(lyst)
        return lyst

    def postorder(self):
        """Returns a list containing the results of
        a postorder traversal."""
        # Exercise
        lyst = []
        self._tree.postorder(lyst)
        return lyst


    def levelorder(self):
        """Returns a list containing the results of
        a levelorder traversal."""
        # Exercise
        lyst = []
        self._tree.levelorder(lyst)
        return lyst

    def remove(self, item):

        def findMax(replacementParent, replacementNode):
            while not replacementNode.getRight().isEmpty():
                replacementParent = replacementNode
                replacementNode = replacementNode.getRight()
            return replacementNode, replacementParent
        
        # This is tricking code with a lot of special cases.
        # I will roughly follow the algorithm on page 762
        if not self.find(item):
            return None

        # find sets self._foundNode and self._foundNodeParent
        current = self._foundNode
        parent = self._foundNodeParent
        currentRoot = current.getRoot()
        left = current.getLeft()
        right = current.getRight()
        if left.isEmpty() and right.isEmpty():  # removing a leaf
            if self._size == 1:  # removing root node since it's the only node
                self._tree = BinaryTree.THE_EMPTY_TREE
            elif item < parent.getRoot():  # removing left child of parent
                parent.setLeft(BinaryTree.THE_EMPTY_TREE)
            else:  # removing right child of parent
                parent.setRight(BinaryTree.THE_EMPTY_TREE)
        elif left.isEmpty(): # removing node with only right child
            if parent == None: # removing root node
                self._tree = right
            elif item < parent.getRoot(): # removing parent's left child
                parent.setLeft(right)
            else:
                parent.setRight(right)
        elif right.isEmpty(): # removing node with only left child
            if parent == None: # removing root node
                self._tree = left
            elif item < parent.getRoot(): # removing parent's left child
                parent.setLeft(left)
            else:
                parent.setRight(left)
        else:  # removing node with two children
            #print "Two children"
            replacementNode, replacementParent = findMax(current, left)
            #print "replacementNode", replacementNode.getRoot(), "replacementParent", replacementParent.getRoot()
            current.setRoot(replacementNode.getRoot())
            # delete replacementNode which might have a left child
            if replacementParent == current:
                current.setLeft(replacementNode.getLeft())
            else:
                replacementParent.setRight(replacementNode.getLeft())
            
        self._size -= 1
        return currentRoot
            

def main():
    tree = BST()
    print "Adding D B A C F E G"
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print tree.find("A")
    print tree.find("Z")

    print "\nString:\n" + str(tree)

    print "Iterator (inorder traversal): "
    iterator = iter(tree)
    while True:
        try:
            print iterator.next(),
        except Exception, e:
            print e
            break
    # Use a for loop instead
    print "\nfor loop (inorder traversal): "
    for item in tree:
        print item,
    print

    print tree
    print '\nRemove "D"', tree.remove("D")
    print tree

    print '\nRemove "C"', tree.remove("C")
    print tree

    print '\nRemove "B"', tree.remove("B")
    print tree

    print '\nRemove "A"', tree.remove("A")
    print tree

    return tree

if __name__ == '__main__': 
    t = main()




