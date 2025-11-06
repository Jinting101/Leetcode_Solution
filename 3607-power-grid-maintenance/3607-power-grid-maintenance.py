class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Union-Find
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        # Build connected components
        for x, y in connections:
            union(x, y)
        
        # Group stations by component, maintaining min heap for each
        component_stations = {}
        for x, y in connections:
            for station in [x, y]:
                root = find(station)
                if root not in component_stations:
                    component_stations[root] = []
                component_stations[root].append(station)
        
        # Remove duplicates and heapify
        for root in component_stations:
            component_stations[root] = list(set(component_stations[root]))
            heapq.heapify(component_stations[root])
        
        offline = set()
        res = []
        
        for action, sid in queries:
            if action == 2:
                offline.add(sid)
            else:  # action == 1
                if sid not in offline:
                    res.append(sid)
                else:
                    # Find the component this station belongs to
                    if sid in parent:
                        root = find(sid)
                        if root in component_stations:
                            # Remove offline stations from heap
                            while component_stations[root] and component_stations[root][0] in offline:
                                heapq.heappop(component_stations[root])
                            
                            if component_stations[root]:
                                res.append(component_stations[root][0])
                            else:
                                res.append(-1)
                        else:
                            res.append(-1)
                    else:
                        res.append(-1)
        
        return res