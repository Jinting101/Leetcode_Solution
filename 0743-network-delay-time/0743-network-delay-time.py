class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for s, e, t in times:
            if s not in adj:
                adj[s] = {}
            adj[s][e] = t
        arrivalT = {k:0}
        visited = set()
        hp = [(0, k)]
        visited.add(k)
        while hp:
            curDist, cur = heapq.heappop(hp)
            if cur not in adj:
                continue
            for nei in adj[cur]:
                if nei not in visited:
                    visited.add(nei)
                    arrivalT[nei] = curDist + adj[cur][nei]
                    heapq.heappush(hp, (arrivalT[nei], nei))
        return max(list(arrivalT.values())) if len(visited) == n else -1

