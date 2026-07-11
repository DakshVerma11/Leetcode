class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #hard question unlikely
        #binary search on the smaller array (so logn is for smaller one)
        #cut1 is mid and cut2 is the next halfs mid (so (n+m+1)//2 -cut1)
        #caculate l1,r2,l2,r2
        #base win case l1<=r2 and l2<=r1 (check odd median or even median)
        #move high lower if l1>r2
        #mode low high else


        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        low = 0
        high = n
        
        while low<=high:
            cut1=(low+high)//2
            cut2=(n+m+1)//2-cut1

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == n else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == m else nums2[cut2]


            if left1<=right2 and left2<=right1:
                if (n + m) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                return max(left1, left2)
            
            elif left1 > right2:
                high = cut1 - 1

            else:
                low = cut1 + 1



