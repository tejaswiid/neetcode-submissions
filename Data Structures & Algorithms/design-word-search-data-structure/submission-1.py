class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.endofword = True
        

    def search(self, word: str) -> bool:
        root = self.root
        def dfs(word,node):
            if not word: return node.endofword
            if word[0] != ".":
                if word[0] not in node.children:
                    return False
                if word[0] in node.children:
                    return dfs(word[1:],node.children[word[0]])
            if word[0] == ".":
                for new in node.children:
                    res = dfs(word[1:],node.children[new])
                    if res: 
                        return res
            return False
        return dfs(word,root)
                
        
