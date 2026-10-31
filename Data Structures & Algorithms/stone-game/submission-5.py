class Solution:
    def stoneGame(self, nums: List[int]) -> str:
        dp = {}
        def dfs(l,r,alice):
            if r < l:
                return 0
            if l == r: 
                if alice:
                    return nums[0]
                else: return 0
            if (l,r,alice) in dp: return dp[(l,r,alice)]
            if alice:
                val1 = nums[l] + dfs(l+1,r,False)
                val2 = nums[r] + dfs(l,r-1,False)
                dp[(l,r,alice)]  = max(val1,val2)
                return dp[(l,r,alice)]
            else:
                val1 = dfs(l+1,r,True)
                val2 = dfs(l,r-1,True)
                dp[(l,r,alice)] =  min(val1,val2)
                return dp[(l,r,alice)]
        alice = dfs(0,len(nums)-1,True)
        bob = sum(nums) - alice
        return True if alice > bob else False
                
            

            

        