class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman-Ford
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            newDist = dist[:]

            for frm, to, price in flights:
                newDist[to] = min(
                    newDist[to],
                    dist[frm] + price
                )

            dist = newDist

        return -1 if dist[dst] == float('inf') else dist[dst]
