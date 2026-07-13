class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pDiag=set()
        nDiag=set()
        
        board=[['.']*n for _ in range(n)]
        res=[]

        def backtracking(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or r+c in pDiag or r-c in nDiag:
                    continue
                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c]='Q'

                backtracking(r+1)

                board[r][c]='.'
                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
        backtracking(0)
        return res

