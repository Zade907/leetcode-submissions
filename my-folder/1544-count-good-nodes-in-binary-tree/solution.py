# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root,maxNode): 
            if root is None: 
                return 
            if root.val >= maxNode:
                self.goodNode += 1 
                maxNode = root.val
            good(root.left,maxNode) 
            good(root.right,maxNode) 
            return self.goodNode 
        self.goodNode = 0 
        n = good(root,root.val) 
        return n
