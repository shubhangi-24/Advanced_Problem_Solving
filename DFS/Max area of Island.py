class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(row,col,grid):
            if row<0 or col<0 or row>len(grid)-1 or col>len(grid[0])-1 or grid[row][col]!=1:
                return 0                                                                        
            direction=[[1,0],[-1,0],[0,1],[0,-1]]
            c=1
            grid[row][col]=2
            for dir in direction:
                new_row=row+dir[0]
                new_col=col+dir[1]
                c=c+dfs(new_row,new_col,grid)
            return c

        m=len(grid)
        n=len(grid[0])
        max_count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count_area=dfs(i,j,grid)
                    max_count=max(count_area,max_count)
        return max_count

        
