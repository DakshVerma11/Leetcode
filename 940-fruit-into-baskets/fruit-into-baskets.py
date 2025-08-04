from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits: return 0
        
        curseq = [[fruits[0], 1], [0, 0]]   # The count for the first fruit should be 1
        fruit_count = 1
        maxfruits = 1
        curtree = set([fruits[0]])
        
        for i in range(1, len(fruits)):    # Start from 1 since 0 is already counted
            if fruits[i] in curtree:
                fruit_count += 1
                if curseq[0][0] == fruits[i]:
                    curseq[0][1] += 1
                else:
                    curseq[0], curseq[1] = curseq[1], curseq[0]
                    curseq[0][1] = 1
                    curseq[0][0] = fruits[i]
            else:
                maxfruits = max(fruit_count, maxfruits)
                fruit_count = curseq[0][1] + 1   # plus the new fruit
                curseq[0], curseq[1] = curseq[1], curseq[0]
                curseq[0][0] = fruits[i]
                curseq[0][1] = 1
                curtree = set([curseq[0][0], curseq[1][0]])   
        
        maxfruits = max(fruit_count, maxfruits) 
        return maxfruits
