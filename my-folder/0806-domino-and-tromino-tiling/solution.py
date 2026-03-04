class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2 
        if n == 3:
            return 5
        arr = [0]*n
        arr[0] = 1
        arr[1] = 2
        arr[2] = 5
        for i in range(3,n):
            arr[i] = arr[i-1] * 2 + arr[i-3]
        return arr[n-1] % (10**9+7)
