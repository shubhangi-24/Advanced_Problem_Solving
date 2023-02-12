class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        ans=0
        while queue:
            cur_row,cur_col,cur_time=queue.popleft()

            if (cur_row-1)>=0 and grid[cur_row-1][cur_col]==1:
                grid[cur_row-1][cur_col]=2
                queue.append((cur_row-1,cur_col,cur_time+1))
                ans=cur_time+1

            if (cur_col+1)<len(grid[0]) and grid[cur_row][cur_col+1]==1:
                grid[cur_row][cur_col+1]=2
                queue.append((cur_row,cur_col+1,cur_time+1))
                ans=cur_time+1
                
            if (cur_col-1)>=0 and grid[cur_row][cur_col-1]==1:
                grid[cur_row][cur_col-1]=2
                queue.append((cur_row,cur_col-1,cur_time+1))
                ans=cur_time+1
                
            if (cur_row+1)<len(grid) and grid[cur_row+1][cur_col]==1:
                grid[cur_row+1][cur_col]=2
                queue.append((cur_row+1,cur_col,cur_time+1))
                ans=cur_time+1
                

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        
        return ans
