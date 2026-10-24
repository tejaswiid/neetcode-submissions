class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.Trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.Trie
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endofword = True

    def search(self, word: str) -> bool:
        node = self.Trie
        for w in word:
            if w not in node.children: return False
            node = node.children[w]
        return node.endofword

    def startsWith(self, prefix: str) -> bool:
        node = self.Trie
        for w in prefix:
            if w not in node.children: return False
            node = node.children[w]
        return True
        
        