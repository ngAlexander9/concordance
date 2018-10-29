"""
dictionary.py
"""
from bst import BST
from avl import AVL
class Entry(object):
    def __init__(self,key,value):
        self.key = key
        self.value = []
        self.value.append(value)
    def __eq__(self, other):
        return self.key == other.key
    def __str__(self):
        return str(self.key) + ":" + str(self.value)
    def addLine(self, value):
        self.value.append(value)

class ListDict(object):
    def __init__(self):
        self._table = []
    def __getitem__(self,key):
        entry = Entry(key,None)
        try:
            index = self._table.index(entry)
            return self._table[index].value
            print "key found"
        except:
            return None
    def __setitem__(self,key,value):
        entry = Entry(key,value)
        try:
            index = self._table.index(entry)
            self._table[index] = entry
        except:
            self._table.append(entry)
            print "key not found adding new key"
            
#BST implementation of Dictionary       
class bstDict(object):
    def __init__(self):
        self._tree = BST()
    def __getitem__(self,key):
        entry = Entry(key, None)
        try:
            return self._tree.find(entry)
        except:
            return None
    def __setitem__(self, key,value):
        entry = Entry(key,value)
        try:
            index = self._tree.find(entry)
            index.addLine(value)
        except:
            self._tree.add(entry)
    def inorder(self):
        lyst = []
        lyst = self._tree.preorder()
        return lyst
        
#AVL implementation of Dictionary
class avlDict(object):
    def __init__(self):
        self._tree = AVL()
    def __getitem__(self,key):
        entry = Entry(key,None)
        try:
            return self._tree.find(entry)
        except:
            return None
    def __setitem__(self,key,value):
        entry = Entry(key,value)
        try:
            index = self._tree.find(entry)
            index.addLine(value)
        except:
            self._tree.add(entry)
    def inorder(self):
        lyst = []
        lyst = self._tree.inorder()
        return lyst
        
