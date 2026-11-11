class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count = {}
        for i in range(len(order)):
            count[order[i]] = i
        for i in range(1,len(words)):
            word1, word2 = words[i-1], words[i]
            l,r = 0, 0 
            while l < len(word1) and r < len(word2) and word1[l] == word2[r]:
                l += 1
                r += 1
            if l < len(word1) and r < len(word2): 
                if count[word1[l]] > count[word2[r]]:
                    return False
                else: 
                    continue
            if l < len(word1) and r == len(word2):
                return False
            
            
           
        return True
        


        