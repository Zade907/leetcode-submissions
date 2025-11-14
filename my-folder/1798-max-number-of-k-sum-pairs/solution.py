class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        counter = 0
        for num in nums :
            comp = k - num
            if comp in freq and freq[comp] > 0:
                freq[comp] -= 1 
                counter += 1 
            else:
                freq[num] = freq.get(num,0) + 1
        print(freq)
        return counter
