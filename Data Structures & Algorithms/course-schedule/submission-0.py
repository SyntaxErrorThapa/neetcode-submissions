class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        visited = set()

        def dfs(node_val):
            # Base case
            if node_val in visited:
                return False 
            
            if preMap[node_val] == []:
                return True

            visited.add(node_val)
            for i in preMap[node_val]:
                if not dfs(i):
                    return False
            visited.remove(node_val)
            preMap[node_val] = []
            
            return True
        
        for num in range(numCourses):
            if not dfs(num): return False
        return True