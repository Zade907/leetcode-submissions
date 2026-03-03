class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(curNum, curList, runningSum):
            if len(curList) == k and runningSum == n:
                res.append(curList[:])
                return
            
            if runningSum > n or len(curList) >= k:
                return 

            for i in range(curNum, 10):
                backtrack(i + 1, curList + [i], runningSum + i)
        backtrack(1,[],0)
        return res
