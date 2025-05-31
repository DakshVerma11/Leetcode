class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        i = 0

        for j in range(len(nums)):
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window:
                return True
            window.add(nums[j])
        
        return False
