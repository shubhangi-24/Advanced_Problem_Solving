class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(row,col,previous_height,heights,ocean):
            if row<0 or row>len(heights)-1 or col<0 or col>len(heights[0])-1:
                return
            if ocean[row][col] or heights[row][col]<previous_height:
                return
            ocean[row][col]=True
            directions =[[1,0],[-1,0],[0,1],[0,-1]]
            for direction in directions:
                new_row=row+direction[0]
                new_col=col+direction[1]
                dfs(new_row,new_col,heights[row][col],heights,ocean)

        pacific=[[0]*len(heights[0]) for _ in range(len(heights))]
        atlantic=[[0]*len(heights[0]) for _ in range(len(heights))]
        rows=len(heights)
        cols=len(heights[0])
        result=[]

        for row in range(rows):
            dfs(row,0,0,heights,pacific)
            dfs(row,cols-1,0,heights,atlantic)

        for col in range(cols):
            dfs(0,col,0,heights,pacific)
            dfs(rows-1,col,0,heights,atlantic)

        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row,col])
        return result
