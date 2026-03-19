class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c = format(c, 'b')
        b = format(b,'b')
        a = format(a, 'b')
        n = max(len(a),len(b),len(c))
        a = a.zfill(n)
        b = b.zfill(n)
        c = c.zfill(n)
        oper = 0
        print(max(a,b,c))
        print(a,b,c, n )
        for i in range(n):
            if int(a[i]) | int(b[i]) != int(c[i]):
                if a[i] == '1' and b[i] == '1' and c[i] == '0':
                    oper += 2
                else:
                    oper += 1
        return oper


