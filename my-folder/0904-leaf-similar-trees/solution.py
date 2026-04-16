# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1Leaves = []
        root2Leaves = []
        def dfs(root, dir):
            if not root:
                return 
            if root.left == None and root.right == None:
                dir.append(root.val)
            dfs(root.left, dir)
            dfs(root.right,dir)
        dfs(root1, root1Leaves)
        dfs(root2, root2Leaves)
        print(root1Leaves, root2Leaves)
        return root1Leaves == root2Leaves
