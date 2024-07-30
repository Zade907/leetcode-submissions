class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        x = str(n)
        for i in x:
            sum += int(i)
            product = product*(int(i))
        return product-sum 
