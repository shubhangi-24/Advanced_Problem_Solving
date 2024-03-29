class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def save_number(digit,row,col):
            rows[row][digit]+=1
            cols[col][digit]+=1
            box_number=(row//3)*3+col//3
            boxes[box_number][digit]+=1

        def can_be_placed(digit,row,col):
            box_n=(row//3)*3+col//3
            if digit not in rows[row] and digit not in cols[col] and digit not in boxes[box_n]:
                return True
            return False

        def place_next_number(row,col):
            if row==N-1 and col==N-1:
                nonlocal sudoku_solved
                sudoku_solved=True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row,col):
            if board[row][col]==".":
                for d in range(1,10):
                    if can_be_placed(d,row,col):
                        save_number(d,row,col)
                        board[row][col]=str(d)
                        place_next_number(row,col)
                        if not sudoku_solved:
                            board[row][col]="."
                            del rows[row][d]
                            del cols[col][d]
                            box_no=(row//3)*3+col//3
                            del boxes[box_no][d]
            else:
                place_next_number(row,col)


        sudoku_solved=False
        N=9
        rows=[defaultdict(int) for i in range(N)]
        cols=[defaultdict(int) for i in range(N)]
        boxes=[defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j]!='.':
                    digit=int(board[i][j])
                    save_number(digit,i,j)
        backtrack(0,0)

        
