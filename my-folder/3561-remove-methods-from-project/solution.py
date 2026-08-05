class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = [False]*n

        adj = [[] for _ in range(n)]
        for u,v in invocations:
            adj[u].append(v)
        
        def dfs(node):
            visited[node] = True
            for neighbors in adj[node]:
                if not visited[neighbors]:
                    dfs(neighbors)
        
        dfs(k)
        defaultAns = list(range(n))
        ans = []
        for i in range(n):
            if not visited[i]:
                ans.append(i)
                for neigh in adj[i]:
                    if visited[neigh]:
                        return defaultAns

        return ans
