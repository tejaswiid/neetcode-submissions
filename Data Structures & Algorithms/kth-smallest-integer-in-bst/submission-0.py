# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                val = q.popleft()
                vals.append(val.val)
                if val.left: q.append(val.left)
                if val.right: q.append(val.right)
        vals.sort()
        return vals[k-1]
        
        
        