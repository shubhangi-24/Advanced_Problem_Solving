class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans=False
        def dfs(row,col,board,word,index):
            if row<0 or row>len(board)-1 or col<0 or col>len(board[0])-1 or board[row][col]!=word[index]:
                return False
            if board[row][col]!='$':
                curchar=board[row][col]
                board[row][col]='$'
                if index==len(word)-1:
                    return True
                ans=False
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for direction in directions:
                    new_row=row + direction[0]
                    new_col=col + direction[1]
                    ans=ans or dfs(new_row,new_col,board,word,index+1)
                    if ans:
                        return True
                board[row][col]=curchar
            return False
        s=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                s.add(board[i][j])
        for ch in word:
            if ch not in s:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                ans=dfs(i,j,board,word,0)
                if ans:
                    return True
        return False
