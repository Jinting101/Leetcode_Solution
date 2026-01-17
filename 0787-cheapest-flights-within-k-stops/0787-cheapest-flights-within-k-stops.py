class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,cost in flights:
            adj[u].append((v, cost))
        visited = set()
        q = [(0, src, 0)]
        while q:
            cost, node, stops = heapq.heappop(q)
            if node == dst:
                if stops <= k+1:
                    return cost
                else:
                    continue
            if node in visited:
                continue
            visited.add(node)
            for nei,cst in adj[node]:
                if nei not in visited:
                    heapq.heappush(q, (cost + cst, nei, stops + 1))
        return -1
