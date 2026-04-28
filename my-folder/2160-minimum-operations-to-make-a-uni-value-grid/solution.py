class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        remainder = grid[0][0] % x
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] % x != remainder:
                    return -1
                nums.append(grid[i][j])
        nums.sort()
        median = nums[len(nums)//2]
        target = median//x
        output = 0
        for i in nums:
            currQuotient = i // x
            output += abs(target - currQuotient)
        return output

