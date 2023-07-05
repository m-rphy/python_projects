#  This is for finding prefix tree. This helps with auto complete

# It is a node of characters ( a - z ) and every node

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False # Mark the end of a work (this indicate it's not the end)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word):
        curr = self.root
        #  Go through every character in 'word'
        for c in word:
            #  If the letter is not a child of the current character
            if c not in curr.children:
                #  Insert a new node
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True # Mark the end of a work (this indicate it is the end)

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
    
    #  Main use case of this data structure
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True