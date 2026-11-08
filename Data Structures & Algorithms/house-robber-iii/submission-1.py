# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(rob,root):
            if not root:
                dp[(rob,root)] = 0
                return 0
            if (rob,root) in dp: return dp[(rob,root)]
            val = 0
            if rob:
                val1 = root.val + dfs(not rob, root.left) + dfs(not rob, root.right)
                val2 = dfs(rob,root.left) + dfs(rob,root.right)
                val = max(val1,val2)
            else:
                val3 = dfs(not rob,root.left) + dfs(not rob, root.right)
                val = val3
            dp[(rob,root)] = val
            return val
        return dfs(True,root)


