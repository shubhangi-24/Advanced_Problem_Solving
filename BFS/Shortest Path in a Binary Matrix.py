class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        if grid[0][0]==1 or grid[row-1][col-1]==1:
            return -1
        grid[0][0]=1
        queue.append((0,0))
        while queue:
            cur_row,cur_col=queue.popleft()
            distance=grid[cur_row][cur_col]
            if cur_row==row-1 and cur_col==col-1:
                return distance
            for direction in directions:
                n_row=cur_row+direction[0]
                n_col=cur_col+direction[1]
                if n_row<row and n_row>=0 and n_col<col and n_col>=0 and grid[n_row][n_col]==0:
                    queue.append((n_row,n_col))
                    grid[n_row][n_col]=distance+1
        return -1




