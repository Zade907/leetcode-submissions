# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        if not root:
            return 
        binary = ""
        def dfs(root, binary):
            if not root:
                return 
            binary += str(root.val)
            if not root.left and not root.right:
                print(binary)
                self.result += int(binary, 2)
                return
            
            dfs(root.left, binary)
            dfs(root.right, binary)

        dfs(root, binary)
        return self.result
