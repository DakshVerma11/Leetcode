class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        
        # Find leftmost occurrence
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        # Check if target exists
        if nums[l] != target:
            return [-1, -1]
        
        left = l
        
        # Find rightmost occurrence
        r = n - 1
        while l < r:
            mid = l + (r - l + 1) // 2  # Upper mid to avoid infinite loop
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        
        return [left, r]