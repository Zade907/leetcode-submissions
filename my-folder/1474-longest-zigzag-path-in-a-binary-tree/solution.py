# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0 

        def dfs(node, currLength, flag):
            if not node:
                return 
            self.maxLength = max(self.maxLength, currLength)
            if flag == "R":
                dfs(node.left, currLength + 1, "L")
                dfs(node.right, 1, "R")
            else:
                dfs(node.right, currLength + 1, "R")
                dfs(node.left, 1, "L")

        dfs(root.left, 1, "L")
        dfs(root.right, 1, "R")
        return self.maxLength
            
