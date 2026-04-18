# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            rightNode = None
            for i in range(n):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(rightNode.left)
                    queue.append(rightNode.right)
            if rightNode:
                result.append(rightNode.val)
        return result
