class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False
    

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        self.root = TrieNode()
        def insert(word):
            node = self.root
            for w in word:
                if w not in node.children:
                    node.children[w] = TrieNode()
                node = node.children[w]
            node.endofword = True
        for word in dictionary:
            insert(word)
        dp = {len(s):0}
        def find(i):
            if i == len(s):
                
                return 0
            if i in dp: return dp[i]
            node = self.root
            # Option 1: Make current character extra
            val = 1 + find(i + 1)
            # Option 2: Try finding dictionary words
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.endofword:
                    val = min(val, find(j + 1))
            dp[i] = val
            return val

        return find(0)
        
        
                
        

        