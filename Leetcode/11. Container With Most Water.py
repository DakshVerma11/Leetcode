class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater=0
        i=0
        j=len(height)-1
        while i<j:
            water=(j - i) * min(height[i], height[j])
            maxwater=max(maxwater,water)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return maxwater 
