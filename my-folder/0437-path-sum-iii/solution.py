# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        from collections import defaultdict
        dict1 = defaultdict(int)
        dict1[0] = 1
        def dfs(root, currSum):
            if root == None:
                return 
            currSum += root.val
            self.count += dict1[currSum - targetSum]

            dict1[currSum] += 1
            dfs(root.left,currSum)
            dfs(root.right,currSum)

            dict1[currSum] -= 1
        dfs(root,0)
        return self.count

