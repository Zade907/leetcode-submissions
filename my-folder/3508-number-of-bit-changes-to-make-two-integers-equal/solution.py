class Solution:
    def minChanges(self, n: int, k: int) -> int:
        count = 0
        if n==k:
            return 0
        else:
            n = bin(n)
            n = n[2:]
            k = bin(k)
            k = k[2:]
            if(len(k)<len(n)):
                k = k.zfill(len(n))
            if(len(k)>len(n)):
                n = n.zfill(len(k))
            print(n,k)
            for i in range (len(n)):
                if(n[i]=="1" and k[i]=="0"):
                    count += 1
                if(n[i]=="0" and k[i]=="1"):
                    return -1
            return count

