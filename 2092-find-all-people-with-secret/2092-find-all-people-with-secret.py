class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                # Always attach to 0's component if possible (secret holder)
                if px == find(0):
                    parent[py] = px
                else:
                    parent[px] = py
        
        # Group meetings by time
        meetings.sort(key=lambda x: x[2])
        
        union(0, firstPerson)
        
        i = 0
        while i < len(meetings):
            time = meetings[i][2]
            group = []
            while i < len(meetings) and meetings[i][2] == time:
                group.append((meetings[i][0], meetings[i][1]))
                i += 1
            
            # Union all meetings at this time
            for p1, p2 in group:
                union(p1, p2)
            
            # Reset those who don't know the secret
            for p1, p2 in group:
                if find(p1) != find(0):
                    parent[p1] = p1
                    parent[p2] = p2
        
        return [i for i in range(n) if find(i) == find(0)]