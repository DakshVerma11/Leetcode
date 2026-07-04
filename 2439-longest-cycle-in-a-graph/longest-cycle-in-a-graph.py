class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = [False] * n
        ans = -1

        def dfs(node):
            nonlocal ans

            depth = {}
            d = 0

            while node != -1:
                if node in depth:
                    ans = max(ans, d - depth[node])
                    break

                if seen[node]:
                    break

                depth[node] = d
                seen[node] = True
                d += 1
                node = edges[node]

        for i in range(n):
            if not seen[i]:
                dfs(i)

        return ans