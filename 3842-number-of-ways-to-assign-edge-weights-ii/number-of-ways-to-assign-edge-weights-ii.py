sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # 1. Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Setup Binary Lifting table
        # LOG is floor(log2(n)) + 1. For n = 10^5, 18 bits is sufficient.
        LOG = 18
        up = [[1] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # 3. DFS to populate immediate parents and depths
        def dfs(node, par, d):
            depth[node] = d
            up[node][0] = par if par != -1 else node
            for neighbor in adj[node]:
                if neighbor != par:
                    dfs(neighbor, node, d + 1)
                    
        dfs(1, -1, 0)
        
        # 4. Populate the full up table for binary lifting
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # 5. Fast LCA lookup function
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring u and v to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both u and v simultaneously
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        # 6. Precompute powers of 2 for O(1) query combinations
        # pow_two[i] stores (2^i) % MOD
        pow_two = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_two[i] = (pow_two[i-1] * 2) % MOD

        # 7. Answer the queries
        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
                continue
                
            lca = get_lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[lca]
            
            # Combinatorics step: 2^(path_len - 1) % MOD
            result.append(pow_two[path_len - 1])
            
        return result