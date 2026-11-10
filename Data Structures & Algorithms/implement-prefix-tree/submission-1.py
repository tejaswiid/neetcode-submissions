class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofnode = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endofnode = True
            
                


    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children: return False
                
            node = node.children[w]
        return node.endofnode == True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children: return False
                
            node = node.children[w]
        return True
        
        