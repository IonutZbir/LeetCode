from typing import Optional, Dict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        return self.bfs(node, visited)

    def bfs(self, node: Optional['Node'], visited: Dict['Node', 'Node']) -> Optional['Node']:
        if node in visited:
            return visited[node]
        
        # Clone the current node
        new_node = Node(node.val)
        visited[node] = new_node

        # Recursively clone the neighbors
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.bfs(neighbor, visited))
        
        return new_node
