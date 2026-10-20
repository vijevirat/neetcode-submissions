class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        grid = [set() for i in range(9)]
        for i in range (0,9):
            for j in range (0,9):
                val = board[i][j]
                if val == '.':
                    continue
                ind = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in grid[ind]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grid[ind].add(val)
        return True

        