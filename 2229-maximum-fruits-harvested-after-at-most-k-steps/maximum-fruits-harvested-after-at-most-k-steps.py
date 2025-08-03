class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        #Search right
        #earch Left 
        #search right then left
        #search left then right


        pos = [f[0] for f in fruits]
        amt = [f[1] for f in fruits]
        n = len(fruits)
        
        prefix = [0]
        for a in amt:
            prefix.append(prefix[-1] + a)
        
        res = 0
        
        # only right from startPos
        left = 0
        right = 0
        while right < n and pos[right] <= startPos + k:
            if pos[right] >= startPos:
                while left < n and pos[left] < startPos:
                    left += 1
                res = max(res, prefix[right+1] - prefix[left])
            right += 1

        #only left from startPos
        left = 0
        right = 0
        while left < n and pos[left] <= startPos:
            # right pointer: largest index <= startPos, but >= startPos - k
            while right < n and pos[right] <= startPos and pos[right] >= startPos - k:
                right += 1
            res = max(res, prefix[right] - prefix[left])
            left += 1
        
        # Case 3 & 4: go left then right, and right then left
        # all subarrays [l, r]
        l = 0
        for r in range(n):
            while l <= r and min(
                abs(startPos - pos[l]) + abs(pos[r] - pos[l]),
                abs(startPos - pos[r]) + abs(pos[r] - pos[l])
            ) > k:
                l += 1
            if l <= r:
                res = max(res, prefix[r+1] - prefix[l])
        
        return res


        