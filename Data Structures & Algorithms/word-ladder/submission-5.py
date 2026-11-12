class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        def diff(w1,w2):
            if len(w1) != len(w2): return False
            ans = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]: ans += 1
            return ans == 1
        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for w in wordList:
                    if w not in visit and diff(w,word):
                        visit.add(w)
                        q.append(w)
            res += 1
        return 0

                    


        