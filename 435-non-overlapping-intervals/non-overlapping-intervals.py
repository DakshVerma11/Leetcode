class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans=-1
        prevEnd=intervals[0][1]

        for start, end in intervals:
            if start>=prevEnd:
                prevEnd= end
            else:
                ans+=1
                prevEnd=min(prevEnd,end)
        return ans if ans>-1 else 0