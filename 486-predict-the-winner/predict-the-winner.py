class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        
        def backtracking(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            pick_left = nums[i] - backtracking(i + 1, j)
            pick_right = nums[j] - backtracking(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
            
        return backtracking(0, len(nums) - 1) >= 0
