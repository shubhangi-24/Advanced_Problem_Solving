class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(ans,output,op,closed):
            if op==0 and closed==0:
                ans.append(output)
            if op>0:
                solve(ans,output+'(',op-1,closed)
            if closed>0 and op<closed:
                solve(ans,output+')',op,closed-1)
        ans=[]
        solve(ans,'',n,n)
        return ans
        
        

           
