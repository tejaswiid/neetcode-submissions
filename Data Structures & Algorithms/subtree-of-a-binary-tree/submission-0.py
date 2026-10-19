# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(p,q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return issame(p.left,q.left) and issame(p.right,q.right)
        def issub(root,subroot):
            if not root and not subroot: return True
            if not root or not subroot: return False
            if root.val == subroot.val:
                val = issame(root,subroot)
                if val: return True
            return issub(root.left,subroot) or issub(root.right,subroot)
        return issub(root,subRoot)
            
            
        