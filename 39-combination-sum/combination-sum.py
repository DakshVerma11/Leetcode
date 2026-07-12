class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(candidates)
        def backtracking(cur,idx):
            if sum(cur)==target:
                res.append(cur.copy())
                return
            if idx>=n or sum(cur)>target:
                return
            

            cur.append(candidates[idx])
            backtracking(cur,idx)
            cur.pop()
            backtracking(cur,idx+1)

        backtracking([],0)
        return res
