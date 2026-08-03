# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = [float("-inf")]
        from collections import deque
        queue = deque([root])
        while queue:
            n = len(queue)
            sum = 0
            for i in range(n):
                node = queue.popleft()
                if node:
                    sum += node.val
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
            result.append(sum)
        return result.index(max(result))
