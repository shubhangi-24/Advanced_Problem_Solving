class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(s,p,i,j,dp):
            if i==0 and j==0:
                return True
            if j==0:
                return False
            if i==0:
                for k in range(j):
                    if p[k]!='*':
                        return False
                return True
            if dp[i-1][j-1]!=-1:
                return dp[i-1][j-1]
            
            if s[i-1]==p[j-1] or p[j-1]=='?':
                dp[i-1][j-1]= solve(s,p,i-1,j-1,dp)

            elif p[j-1]=='*':
                dp[i-1][j-1] =solve(s,p,i-1,j,dp) or solve(s,p,i,j-1,dp)
            else:
                dp[i-1][j-1]=False
            return dp[i-1][j-1]
        
        dp=[[-1]*len(p) for _ in range(len(s))]
        return solve(s,p,len(s),len(p),dp)
