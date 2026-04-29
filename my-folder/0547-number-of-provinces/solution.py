class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n
        provinces = 0

        def dfs(city):
            visited[city] = 1
            for i in range(n):
                if isConnected[city][i] == 1 and not visited[i]:
                    dfs(i)
        for j in range(n):
            if visited[j] == 0:
                provinces += 1
                dfs(j)
        return provinces
