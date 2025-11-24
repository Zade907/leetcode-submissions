# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaf(root,leaves):
            if root is None:
                return
            if root.right == None and root.left == None:
                leaves.append(root.val)
            else:
                leaf(root.left,leaves)
                leaf(root.right,leaves)
            return leaves
        leave1,leave2 = [],[]
        tree1 = leaf(root1,leave1)
        tree2 = leaf(root2,leave2)
        return tree1 == tree2
        

