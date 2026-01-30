# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([root])
        maxSum = root.val 
        level = 1
        currLevel = 1
        while q:
            n = len(q)
            tempSum = 0
            for i in range(n):
                node = q.popleft()
                if node:
                    tempSum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if tempSum > maxSum: 
                maxSum = tempSum
                level = currLevel
            currLevel += 1
        return level

