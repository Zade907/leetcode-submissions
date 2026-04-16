# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, prevMax):
            if root is None:
                return 
            if root.val >= prevMax:
                prevMax = root.val
                self.count += 1
            dfs(root.left, prevMax)
            dfs(root.right, prevMax)
            return self.count
        dfs(root,root.val)
        return self.count

