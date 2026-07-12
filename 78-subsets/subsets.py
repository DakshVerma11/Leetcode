class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtracking(cur,idx):
            if idx==n:
                res.append(cur[::])
                return
            cur.append(nums[idx])
            backtracking(cur,idx+1)
            cur.pop()
            backtracking(cur,idx+1)
        backtracking([],0)
        return res