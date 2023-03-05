class Solution:
    def numDecodings(self, s: str) -> int:

        def solve(s,i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            left = solve(s,i+1)
            right=0
            if (i+1 < len(s)) and (s[i]=='1' or (s[i]=='2' and s[i+1] < '7')): 
                right = solve(s,i+2)
            ans=left+right
            dp[i]=ans
            return dp[i]

        dp=[-1]*len(s)
        if len(s)==0:
            return 0
        return solve(s,0)
