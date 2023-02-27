class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(grid,row,col,prev,dp):
            if row<0 or row>len(matrix)-1 or col<0 or col>len(matrix[0])-1 or grid[row][col]<=prev:
                return 0
            if dp[row][col]!=-1:
                return dp[row][col]

            s=0
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                new_row=row+direction[0]
                new_col=col+direction[1]
                s=max(s,dfs(grid,new_row,new_col,grid[row][col],dp)+1)

            dp[row][col]=s
            return dp[row][col]

        dp=[[-1 for _ in range(len(matrix[0]))]for _ in range(len(matrix)) ]
        max_d=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c=dfs(matrix,i,j,-1,dp)
                max_d=max(max_d,c)
        return max_d
