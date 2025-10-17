class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        current = ""
        reps = 0
        for i in range (len(chars)):
            current =  chars[i]
            reps += 1
            if((i+1 < len(chars) and chars[i+1] != current) or (i == len(chars) - 1)):
                s += current 
                if reps != 1 : s += str(reps)
                reps = 0
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
            
