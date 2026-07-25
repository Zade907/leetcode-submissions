# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        self.count = 0
        freq[0] = 1
        def dfs(node, currSum):
            if not node:
                return

            currSum += node.val
            self.count += freq[currSum - targetSum]

            freq[currSum] += 1
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            freq[currSum] -= 1
            return self.count
        dfs(root, 0)
        return self.count
