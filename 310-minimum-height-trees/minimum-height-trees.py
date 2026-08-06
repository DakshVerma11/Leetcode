class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Time Complexity: O(V + E)
        # Space Complexity: O(V
        # Intuition: Find the centroids of the tree by stripping leaf nodes layer by layer 
        # using a BFS-based topological sort until only 1 or 2 core nodes remain.

        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()

        for src, neighbors in adj.items():
            edge_cnt[src] = len(neighbors)
            if len(neighbors) == 1:
                leaves.append(src)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
