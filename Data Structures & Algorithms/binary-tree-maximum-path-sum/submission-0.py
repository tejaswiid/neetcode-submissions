# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def dfs(root):
            if not root: return float("-inf")
            path_left = dfs(root.left)
            path_right = dfs(root.right)
            path_sum = max(path_left+root.val,
                           path_right+root.val,
                           root.val)
            self.max_sum = max(self.max_sum,path_sum,path_left+path_right+root.val)
            return path_sum
        dfs(root)
        return self.max_sum
            



        