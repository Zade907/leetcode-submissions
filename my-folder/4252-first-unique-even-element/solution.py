class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        queue = []
        visited = []
        for i in nums:
            if i % 2 == 0:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                elif i in queue and i in visited:
                    queue.remove(i)
        return queue[0] if queue else -1
                
