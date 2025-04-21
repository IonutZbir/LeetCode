from typing import List

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = {}

        for (a, b), val in zip(equations, values):
            edges = graph.get(a, [])
            edges.append((b, val))
            graph[a] = edges

            edges = graph.get(b, [])
            edges.append((a, 1 / val))
            graph[b] = edges

        # print(graph)

        res = []
        for start, end in queries:
            r = self.bfs(graph, start, end)
            if r == None:
                r = -1
            res.append(r)

        return res

    def bfs(self, graph, start, end):

        # calcola l'albero dei cammini minimi partendo da start, poi effettua una visita su quest'albero,
        # trovando il cammino da start -> end e poi moltiplica i pesi

        visited = set()
        queue = [start]
        tree = {}
        flag = True
        while queue and flag:
            nd = queue.pop(0)
            if nd not in visited:
                visited.add(nd)
                edges = tree.get(nd, [])

                try:
                    for neighbor, weight in graph[nd]:
                        # print(f"{nd, neighbor, weight}")

                        if neighbor not in visited:
                            edges.append((neighbor, weight))
                            queue.append(neighbor)
                    
                    tree[nd] = edges
                    
                except KeyError:
                    return -1

        # print(f"{tree}")

        res = self.dfs(tree, start, end)

        return res
    
    def dfs(self, graph, start, end, visited=None):
        if visited is None:
            visited = set()
        
        if start == end:
            return 1
        
        visited.add(start)

        for neighbor, weight in graph[start]:
            if neighbor not in visited:
                res = self.dfs(graph, neighbor, end, visited)
                if res is not None:
                    return res * weight
        
        return None

equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
values = [3.0, 4.0, 5.0, 6.0]
queries = [
    ["x1", "x5"],
    ["x5", "x2"],
    ["x2", "x4"],
    ["x2", "x2"],
    ["x2", "x9"],
    ["x9", "x9"],
]

s = Solution()
res = s.calcEquation(equations, values, queries)
print(res)
