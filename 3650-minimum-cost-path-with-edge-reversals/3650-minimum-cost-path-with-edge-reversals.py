class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,c in edges:
            adj[u].append((v, c))
            adj[v].append((u,2*c))
        visited = set()
        q = [(0, 0)]
        while q:
            cost, node = heapq.heappop(q)
            if node == n-1:
                return cost
            if node in visited:
                continue
            visited.add(node)
            for nei,c in adj[node]:
                if nei not in visited:
                    heapq.heappush(q, (cost+c, nei))
        return -1
            