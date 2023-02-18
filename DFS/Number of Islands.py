class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col,grid):
            if row<0 or row>len(grid)-1 or col<0 or col>len(grid[0])-1 or grid[row][col]!="1":
                return 
            grid[row][col]=2
            direction=[[-1,0],[1,0],[0,1],[0,-1]]
            for dir in direction:
                new_row=row+dir[0]
                new_col=col+dir[1]
                dfs(new_row,new_col,grid)
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j,grid)
                    c+=1
        return c
