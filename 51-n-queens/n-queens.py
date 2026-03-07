class Solution:
    def solveNQueens(self, n: int):
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        placement = [-1] * n
        res = []

        def backtrack(r: int):
            if r == n:
                board = []
                for i in range(n):
                    row = ['.'] * n
                    row[placement[i]] = 'Q'
                    board.append(''.join(row))
                res.append(board)
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                placement[r] = c
                cols.add(c); diag1.add(r - c); diag2.add(r + c)
                backtrack(r + 1)
                cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)

        backtrack(0)
        return res