# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
         self.maxLength = 0
         def longestPath(node,flag,length):
            if not node: 
                return 
            self.maxLength = max(length,self.maxLength)
            if flag == "R":
                longestPath(node.left, 'L', length + 1)
                longestPath(node.right, 'R', 1)
            else:
                longestPath(node.left, 'L',  1)
                longestPath(node.right, 'R', length + 1)

        
         longestPath(root, 'R', 0)
         longestPath(root, 'L', 0)
         return self.maxLength
                




