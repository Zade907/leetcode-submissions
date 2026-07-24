# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leafNodes):
            if not root:
                return 
            if not root.right and not root.left:
                leafNodes.append(root.val)
            else:
                dfs(root.left, leafNodes)
                dfs(root.right,leafNodes)
            return leafNodes
        leafNode1 = dfs(root1, [])
        leafNode2 = dfs(root2, [])
        return leafNode1 == leafNode2
