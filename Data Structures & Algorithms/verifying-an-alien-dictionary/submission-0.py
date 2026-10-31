class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = defaultdict(int)

        for i, o in enumerate(order):
            count[o] = i

        def isit(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if count[w1[i]] < count[w2[i]]:
                    return True
                elif count[w1[i]] > count[w2[i]]:
                    return False

            return len(w1) <= len(w2)

        for i in range(1, len(words)):
            if not isit(words[i-1], words[i]):
                return False

        return True