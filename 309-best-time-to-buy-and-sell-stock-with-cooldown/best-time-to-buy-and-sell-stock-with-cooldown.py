class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp={}
        def backtracking(idx, canBuy):
            if idx>=n:
                return 0
            if (idx,canBuy) in dp:
                return dp[(idx,canBuy)]
            dontDoAnythingToday=backtracking(idx+1,canBuy)
            if canBuy:
                buyToday=backtracking(idx+1,False)-prices[idx]
                dp[(idx,canBuy)]=max(dontDoAnythingToday,buyToday)
            else:
                sellToday=backtracking(idx+2,True)+prices[idx]
                dp[(idx,canBuy)]=max(dontDoAnythingToday,sellToday)
            return dp[(idx,canBuy)]
        return backtracking(0,True)