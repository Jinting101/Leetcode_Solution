class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize graph
        graph = {i: set() for i in range(numCourses)}  # List of immediate prerequisites
        
        # Build graph with immediate prerequisites
        for x, y in prerequisites:
            graph[x].add(y)
        
        # This will store all prerequisites for each course
        all_prerequisites = {i: set() for i in range(numCourses)}
        
        def dfs(course):
            # If we already computed the prerequisites for this course, return it
            if all_prerequisites[course]:
                return all_prerequisites[course]
            
            # Add the direct prerequisites first
            prerequisites_set = set(graph[course])
            
            # Then, for each prerequisite, accumulate their prerequisites
            for prerequisite in graph[course]:
                prerequisites_set.update(dfs(prerequisite))
            
            # Store the result in the dictionary
            all_prerequisites[course] = prerequisites_set
            return prerequisites_set
        
        # Compute all prerequisites for each course
        for course in range(numCourses):
            if not all_prerequisites[course]:  # If we haven't computed it yet
                dfs(course)
        
        # Answer the queries
        result = []
        for x, y in queries:
            result.append(y in all_prerequisites[x])
        
        return result
