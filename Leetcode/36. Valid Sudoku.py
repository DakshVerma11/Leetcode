class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                # Row check
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                
                # Column check
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                
                # Sub-box check
                row_idx = 3 * (i // 3)
                col_idx = 3 * (i % 3)
                val = board[row_idx + j // 3][col_idx + j % 3]
                if val != '.':
                    if val in box:
                        return False
                    box.add(val)
        
        return True
