"""
regex.py
"""
import re
from dictionary import bstDict
from dictionary import avlDict
from time import clock
#Begin parsing words from file
#regex for words
regex = r'[\w+-?\'?]*\w+'
wordsearch = re.compile(regex,re.IGNORECASE)

stopFile = "stop_words.txt"
z = open(stopFile, 'r')
stopWords = z.readlines()
stopWords = [x.strip() for x in stopWords]

#file handler
fileName = "hw5data.txt"
f = open(fileName, 'r')

#list of strings by line
textRaw = f.readlines()

#list of lists of words by line
textWords = []
for x in textRaw:
    textWords.append(wordsearch.findall(x))
#End parsing words from file

#associates line numbers to words - test parser
"""
for lineNum in xrange(len(textWords)):
    for word in textWords[lineNum]:
        if not word.lower() in stopWords:
            print str(lineNum+1) + ": " + word.lower()
"""

#bst Implementation
b = bstDict()
bstart = clock()
for lineNum in xrange(len(textWords)):
    for word in textWords[lineNum]:
        if not word.lower() in stopWords:
            #adds new entry at for the word (+1 to account for starting from 0)
            b[word.lower()] = lineNum+1
bend = clock()
brunTime = bend-bstart
z = b.inorder()
for x in z:
    print x
print "----------------------------"
#avl implementation
a = avlDict()
astart=clock()
for lineNum in xrange(len(textWords)):
    for word in textWords[lineNum]:
        if not word.lower() in stopWords:
            #adds new entry at for the word (+1 to account for starting from 0)
            a[word.lower()] = lineNum+1
aend = clock()
arunTime = aend-astart
z = a.inorder()
for x in z:
    print x
print "----------------------------"
print "BST Implementation: %.6f sec" % (brunTime)
print "AVL Implementation: %.6f sec" % (arunTime)
