class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m=len(nums1),len(nums2)
        mid = (n+m)>>1
        is_even = ((n+m) % 2 == 0)
        
        i = j = 0
        prev = curr = 0
        
        for _ in range(mid + 1):
            prev = curr
            if i < n and (j >= m or nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        return (prev + curr) / 2.0 if is_even else curr
