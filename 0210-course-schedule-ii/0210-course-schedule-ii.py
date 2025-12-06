class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for x,y in prerequisites:
            adj[y].append(x)
            indegrees[x] += 1
        deq = deque([i for i in range(numCourses) if indegrees[i] == 0])
        order = []
        while deq:
            node = deq.popleft()
            order.append(node)
            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    deq.append(nei)
        return order if len(order) == numCourses else []