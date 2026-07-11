class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h<len(piles):
            return -1
        def canEatAllBananas(rate):
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/rate)
            return hours<=h
        l=1
        r=max(piles)

        while l<r:
            mid=(l+r)//2

            if canEatAllBananas(mid):
                r=mid
            else:
                l=mid+1
        
        return r 