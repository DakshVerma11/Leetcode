class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        
        for num in nums:
            maxOR |= num
        
        count = 0
        n = len(nums)
        
        def dfs(i, curOR):
            nonlocal count
            
            if i == n:
                if curOR == maxOR:
                    count += 1
                return
            
            dfs(i + 1, curOR | nums[i])
            dfs(i + 1, curOR)
        
        dfs(0, 0)
        
        return count
