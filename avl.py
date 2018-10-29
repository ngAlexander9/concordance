from bst import BST
from binarytreeAVL import BinaryTreeAVL

class AVL(BST):
    def __init__(self):
        BST.__init__(self)

    def add(self, newItem):
        """Adds newItem to the tree."""

        # Helper function to search for item's position 
        def addHelper(tree):

            def rotateLeft(tree):
                newTree = BinaryTreeAVL(tree.getRoot())
                newTree.setLeft(tree.getLeft())
                newTree.setRight(tree.getRight().getLeft())
                newTree.setBalance(tree.getBalance())
                tree.setRoot(tree.getRight().getRoot())
                tree.setBalance(tree.getRight().getBalance())
                tree.setLeft(newTree)
                tree.setRight(tree.getRight().getRight())

            def rotateRight(tree):
                newTree = BinaryTreeAVL(tree.getRoot())
                newTree.setRight(tree.getRight())
                newTree.setLeft(tree.getLeft().getRight())
                newTree.setBalance(tree.getBalance())
                tree.setRoot(tree.getLeft().getRoot())
                tree.setBalance(tree.getLeft().getBalance())
                tree.setRight(newTree)
                tree.setLeft(tree.getLeft().getLeft())


            # start of addHelper code
            currentItem = tree.getRoot()
            left = tree.getLeft()
            right = tree.getRight()

            if newItem < currentItem:
                if not tree.getLeft().isEmpty():
                    tallerLeftSubtree = addHelper(left)
                    if tallerLeftSubtree:
                        if tree.getBalance() == 'TR':
                            tree.setBalance('EQ')
                            return False
                        elif tree.getBalance() == 'EQ':
                            tree.setBalance('TL')
                            return True
                        else:
                            if tree.getLeft().getBalance() == 'TL':
                                tree.setBalance('EQ')
                                tree.getLeft().setBalance('EQ')
                            else:
                                if tree.getLeft().getRight().getBalance() == 'TL':
                                    tree.setBalance('TR')
                                    tree.getLeft().setBalance('EQ')
                                elif tree.getLeft().getRight().getBalance() == 'TR':
                                    tree.setBalance('EQ')
                                    tree.getLeft().setBalance('TR')
                                else:
                                    tree.setBalance('EQ')
                                    tree.getLeft().setBalance('EQ')

                                tree.getLeft().getRight().setBalance('EQ')
                                rotateLeft(tree.getLeft())
                            rotateRight(tree)
                            return False
                else:
                    tree.setLeft(BinaryTreeAVL(newItem))
                    if tree.getBalance() == 'EQ':
                        tree.setBalance('TL')
                        return True
                    else:
                        tree.setBalance('EQ')
                        return False

            else: # newItem > currentItem
                if not tree.getRight().isEmpty():
                    tallerRightSubtree = addHelper(right)
                    if tallerRightSubtree:
                        if tree.getBalance() == 'TL':
                            tree.setBalance('EQ')
                            return False
                        elif tree.getBalance() == 'EQ':
                            tree.setBalance('TR')
                            return True
                        else: # Two too tall on right now
                            if tree.getRight().getBalance() == 'TR': #only rotate left on self
                                tree.setBalance('EQ')
                                tree.getRight().setBalance('EQ')
                            else: # need to rotate right around right child, then rotate left on self
                                if tree.getRight().getLeft().getBalance() == 'TR':
                                    tree.setBalance('TL')
                                    tree.getRight().setBalance('EQ')
                                elif tree.getRight().getLeft().getBalance() == 'TL':
                                    tree.setBalance('EQ')
                                    tree.getRight().setBalance('TR')
                                else:
                                    tree.setBalance('EQ')
                                    tree.getRight().setBalance('EQ')
                                    
                                tree.getRight().getLeft().setBalance('EQ')
                                rotateRight(tree.getRight())
                            rotateLeft(tree)
                            return False
                else:
                    tree.setRight(BinaryTreeAVL(newItem))
                    if tree.getBalance() == 'EQ':
                        tree.setBalance('TR')
                        return True
                    else:
                        tree.setBalance('EQ')
                        return False

            # End of addHelper

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTreeAVL(newItem)

        # Otherwise, search for the item's spot
        else:
            addHelper(self._tree)
        self._size += 1
        
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
