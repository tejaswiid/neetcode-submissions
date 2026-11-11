# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""
        def dfs(root):
            if not root:
                self.res += "N "
                return 
            self.res += str(root.val)
            self.res += " "
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split()
        print(vals)
        self.i = 0
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()












