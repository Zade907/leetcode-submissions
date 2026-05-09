class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        nums = ["0","1","2","3","4","5","6"]
        for i in events:
            if i == "W":
                counter += 1 
                if counter == 10:
                    return [score,counter]
            else:
                if i in nums:
                    score += int(i)
                else:
                    score += 1
        return [score,counter]
