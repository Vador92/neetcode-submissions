class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # run through the rows and cols
        for i in range(len(board)):
            rows = set()
            cols = set()
            for j in range(len(board[0])):
                if board[i][j] in rows:
                    return False
                elif board[i][j] != ".":
                    rows.add(board[i][j])

                if board[j][i] in cols:
                    return False
                elif board[j][i] != ".":
                    cols.add(board[j][i])
        
        r,c = 1, 1
        while r <= 8 and c <= 8:
            box = set()
            if board[r][c] != ".":
                box.add(board[r][c])
            for dx, dy in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                if board[r + dx][c + dy] in box:
                    return False
                elif board[r + dx][c + dy] != ".":
                    box.add(board[r + dx][c + dy])

            if c != 8:
                c += 3
            else:
                r += 3
                c = 1

        return True

