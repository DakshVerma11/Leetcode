class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        #basket_used = [False] * n 
        unplaced_fruits = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0 
                    placed = True
                    break
            if not placed:
                unplaced_fruits += 1 

        return unplaced_fruits