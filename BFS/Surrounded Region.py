class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        queue=deque()
        visited=[[False]* cols for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i==0 or i==rows-1 or j==0 or j==cols-1:
                    if board[i][j]=='O':
                        queue.append((i,j))
                        visited[i][j]=True
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            r,c=queue.popleft()
            for direction in directions:
                n_row=r+direction[0]
                n_col=c+direction[1]
                if 0<=n_row<rows and 0<=n_col<cols and board[n_row][n_col]=='O' and not visited[n_row][n_col]:
                    visited[n_row][n_col]=True
                    queue.append((n_row,n_col))

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and not visited[i][j]:
                    board[i][j]='X'
