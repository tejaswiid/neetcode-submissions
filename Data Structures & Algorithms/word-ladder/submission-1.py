class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        def diff(word1,word2):
            if len(word1) != len(word2):
                return False
            res = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    res += 1
            return res == 1
        dp = {}
        def dfs(word):
            if word == endWord:
                return 1
            if word in dp: return dp[word]
            dp[word] = float("inf")
            for w in wordList:
                if diff(w,word):
                    dp[word] = min( dp[word],1+dfs(w))
            return dp[word]
        res =dfs(beginWord) 
        return res if res != float("inf") else 0
        