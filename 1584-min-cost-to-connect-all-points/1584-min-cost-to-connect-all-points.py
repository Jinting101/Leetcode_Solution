class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(dict)
        n = len(points)
        for i,point1 in enumerate(points):
            a, b = point1
            for j in range(i+1, n):
                c, d = points[j]
                dist = abs(a-c) + abs(b-d)
                adj[(a,b)][(c,d)] = dist
                adj[(c,d)][(a,b)] = dist
        res = 0
        q = [(0, points[0][0], points[0][1])]
        visited = set()
        while q:
            cost, x, y = heapq.heappop(q)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            res += cost
            for new_point in adj[(x,y)]:
                c, d = new_point
                dist = adj[(x,y)][new_point]
                if new_point not in visited:
                    heapq.heappush(q, (dist, c, d))
        return res

        
                    
    
        # {(0,0):{(2,2): 4, (5,2):7}
        # (4,2),(7,3),(7,4),(13,5)

        # pop 4: 1-2 connected:

        # (3,3),(7,4),(7,3),(7,4),(13,5)
        # (dist, nei)

        # pop 3: 2-3 connected:

        # 4,7,7,7,9,10,13

        # pop 4: 3-4 connected:


