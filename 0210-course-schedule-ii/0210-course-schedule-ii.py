class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        
        res = []
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in graph[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        if len(res) == numCourses:
            return res
        return []
