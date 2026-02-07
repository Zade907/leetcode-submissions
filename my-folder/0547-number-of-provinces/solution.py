class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        provinces = 0

        def dfs(i):
            if visited[i] == 0:
                visited[i] = 1
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        return provinces

        


