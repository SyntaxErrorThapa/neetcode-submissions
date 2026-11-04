class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}

        # Remember its bidirectional
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(node):
            visited.add(node)
            for i in adj[node]:
                if i not in visited:
                    dfs(i)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count