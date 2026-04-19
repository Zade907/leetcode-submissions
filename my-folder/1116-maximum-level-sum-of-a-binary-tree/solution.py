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
        maxSum = float("-inf")
        bestLevel = 1
        curLevel = 0
        while q:
            n = len(q)
            curSum = 0
            
            for i in range(n):
                node = q.popleft()
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curLevel += 1
            if curSum > maxSum:
                maxSum = curSum 
                bestLevel = curLevel
        return bestLevel



