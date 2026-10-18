class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for st in strs:
            val = sorted(st)
            
            hash_map["".join(val)].append(st)
        res = []
        for k,v in hash_map.items():
            res.append(v)
        return res
        