class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(conditions):

            adj = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1

            q = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            order = []

            while q:
                node = q.popleft()
                order.append(node)

                for neighbor in adj[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            if len(order) != k:
                return []

            return order

        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)

        if not rowOrder or not colOrder:
            return []

        rowPos = [0] * (k + 1)
        colPos = [0] * (k + 1)

        for i, value in enumerate(rowOrder):
            rowPos[value] = i

        for i, value in enumerate(colOrder):
            colPos[value] = i

        matrix = [[0] * k for _ in range(k)]

        for value in range(1, k + 1):
            matrix[rowPos[value]][colPos[value]] = value

        return matrix