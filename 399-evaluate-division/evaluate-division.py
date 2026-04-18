class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, end, visited)
                    if product != -1.0:
                        return weight * product
            return -1.0

        results = []
        for c, d in queries:
            results.append(dfs(c, d, set()))
            
        return results