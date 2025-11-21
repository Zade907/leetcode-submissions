class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        senate = list(senate)
        D, R = deque(), deque()
        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            if D[0] < R[0]:
                D.append(D[0]+len(senate))
                R.popleft()
                D.popleft()
            else:
                R.append(R[0]+len(senate))
                R.popleft()
                D.popleft()

        return "Radiant" if R else "Dire"

            
