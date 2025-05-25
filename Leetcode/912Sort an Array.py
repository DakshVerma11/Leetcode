import random
class Solution:
    def quickSort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, high)

    def partition(self, nums, low, high):
        rand_idx = random.randint(low, high)
        nums[high], nums[rand_idx] = nums[rand_idx], nums[high]  # random pivot
        pivot = nums[high]
        j = low - 1
        for i in range(low, high):
            if nums[i] <= pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[j + 1], nums[high] = nums[high], nums[j + 1]
        return j + 1

    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums



class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged






class Solution:
    def sortArray(self, nums):
        if not nums:
            return []
        
        min_val = min(nums)
        max_val = max(nums)
        
        size = max_val - min_val + 1
        count = [0] * size
        
        for num in nums:
            count[num - min_val] += 1
        
        sorted_nums = []
        for i, freq in enumerate(count):
            sorted_nums.extend([i + min_val] * freq)
        
        return sorted_nums







