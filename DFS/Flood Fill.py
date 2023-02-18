class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row,col,image,oldColor,color):
            if row<0 or row>len(image)-1 or col<0 or col>len(image[0])-1 or image[row][col]!=oldColor:
                return 
            image[row][col]=color
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for direction in directions:
                new_row=row+direction[0]
                new_col=col+direction[1]
                dfs(new_row,new_col,image,oldColor,color)
        
        if image[sr][sc]!=color:
            dfs(sr,sc,image,image[sr][sc],color)
        return image
