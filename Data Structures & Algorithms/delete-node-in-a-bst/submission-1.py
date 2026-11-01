# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root,key):
            if not root: return None
            if root.val == key:
                left = root.left
                right = root.right
                if not left and not right:
                    return None
                if left and not right: 
                    return left
                if right and not left:
                    return right
                curr = right
                while curr.left:
                    curr = curr.left
                curr.left = left
                return right
            if root.val < key:
                root.right = dfs(root.right,key)
            else:
                root.left = dfs(root.left,key)
            return root
        return dfs(root,key)

        