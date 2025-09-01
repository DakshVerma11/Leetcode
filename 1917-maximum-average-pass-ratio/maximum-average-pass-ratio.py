import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(pass_count, total_count):
            return (pass_count + 1) / (total_count + 1) - pass_count / total_count
        
        maxheap = []
        for pass_count, total_count in classes:
            heapq.heappush(maxheap, (-gain(pass_count, total_count), pass_count, total_count))
        
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(maxheap)
            p += 1
            t += 1
            heapq.heappush(maxheap, (-gain(p, t), p, t))
        
        total_ratio = 0
        for _, p, t in maxheap:
            total_ratio += p / t
        
        return total_ratio / len(classes)
