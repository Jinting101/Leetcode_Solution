class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        gg = [[] for _ in range(n)]
        outdegrees = [0] * n
        for i,x in enumerate(graph):
            for y in x:
                gg[y].append(i)
            outdegrees[i] += len(x)
        q = deque()
        for i in range(n):
            if outdegrees[i] == 0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in gg[cur]:
                outdegrees[nei] -= 1
                if outdegrees[nei] == 0:
                    res.append(nei)
        return sorted(res)




        n = len(graph)
        res = []
        visited = set()
        memo = [0] * n
        
        def dfs(i):
            if memo[i] == 1 or len(graph[i]) == 0:
                return True
            # the latter condition is used to detect cycles
            elif memo[i] == -1 or i in visited:
                return False
            
            visited.add(i)
            
            for neighbour in graph[i]:
                if not dfs(neighbour):
                    memo[i] = -1
                    return False

            memo[i] = 1
            return True
        
        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
