class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t, v))
        visited = set()
        q = [(0, k)]
        res = [0]
        while q:
            time, node = heapq.heappop(q)
            if node in visited:
                continue
            res[0] = max(res[0], time)
            visited.add(node)
            for t, nei in adj[node]:
                heapq.heappush(q, (t+time, nei))
        if len(visited) == n:
            return res[0]
        return -1