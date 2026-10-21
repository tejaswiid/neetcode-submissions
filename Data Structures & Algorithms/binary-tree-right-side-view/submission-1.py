# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)
        if not root: return []
        while q:
            v = 0 
            for _ in range(len(q)):
                v = q.popleft()
                if v.left: q.append(v.left)
                if v.right: q.append(v.right)
            res.append(v.val)
        return res
        