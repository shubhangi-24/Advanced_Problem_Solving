class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def solve(stone,i):
            if i>=len(stone):
                return 0
            if dp[i]!=-1:
                return dp[i]
            a=b=c=float("-inf")
            a=stone[i]-solve(stone,i+1)
            if i+1<len(stone):
                b=stone[i]+stone[i+1]-solve(stone,i+2)
            if i+2<len(stone):
                c=stone[i]+stone[i+1]+stone[i+2]-solve(stone,i+3)
            ans=max(a,max(b,c))
            dp[i]=ans
            return dp[i]

        
        dp=[-1]*(len(stoneValue))
        score=solve(stoneValue,0)
        if score==0:
            return "Tie"
        elif score>0:
            return "Alice"
        else:
            return "Bob"
