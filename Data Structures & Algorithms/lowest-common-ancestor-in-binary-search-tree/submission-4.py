# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = []
        def dfs(root):
            if not root: return []
            vals = []
            vals.append(root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            vals.extend(left)
            vals.extend(right)
            if ((p.val in left and q.val in right) or
                (q.val in left and p.val in right) or
                (root.val == p.val and q.val in vals) or
                (root.val == q.val and p.val in vals)):
                res.append(root)
            return vals
        dfs(root)
        # res.sort()
        return res[-1]
        # print(res)
            







        