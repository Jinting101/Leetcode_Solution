class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        memo = {}
        adj = defaultdict(list)
        for x,y,z in zip(original, changed, cost):
            adj[x].append((y, z))
        
        def cost_of_change(st, ed):
            visited = set()
            q = [(0, st)]
            while q:
                cost, node = heapq.heappop(q)
                if node == ed:
                    return cost
                if node in visited:
                    continue
                visited.add(node)
                for nei,c in adj[node]:
                    if nei not in visited:
                        heapq.heappush(q, (cost+c, nei))
            return -1
        
        res = 0
        for a,b in zip(source, target):
            if a == b:
                continue
            if (a,b) in memo:
                res += memo[(a,b)]
                continue
            cur = cost_of_change(a, b)
            if cur == -1:
                return -1
            res += cur
            memo[(a, b)] = cur
        return res


                


