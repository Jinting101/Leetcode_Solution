class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = [0]*numCourses
        for v,u in prerequisites:
            adj[u].append(v)
            indegrees[v] += 1
        q = deque([i for i,x in enumerate(indegrees) if x == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        if len(order) == numCourses:
            return order
        return []
        
        # (0, 1) means 1 -> 0

        # 0 -> 1

        # 0 -> 1
        # 0 -> 2
        # 1 -> 3
        # 2 -> 3