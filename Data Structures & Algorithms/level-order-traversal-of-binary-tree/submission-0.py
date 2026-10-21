# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        if not root: return []
        res = []
        while q:
            vals = []
            for _ in range(len(q)):
                v = q.popleft()
                vals.append(v.val)
                if v.left: q.append(v.left)
                if v.right: q.append(v.right)
            # print(vals)
            res.append(vals)
        return res
        