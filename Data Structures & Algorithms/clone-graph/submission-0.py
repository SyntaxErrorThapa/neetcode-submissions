"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic = {}

        def helper(node):
            # Base Case 
            if node in dic:
                return dic[node]
            
            copy = Node(node.val)
            dic[node] = copy
            # Add the neighbour for the copy
            for n in node.neighbors:
                copy.neighbors.append(helper(n))
            
            return copy
        
        return helper(node) if node else None