class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(s1,s2,m,n):
            if m==0 and n==0:
                return 0
            if m==0:
                return n
            if n==0:
                return m
            if dp[m-1][n-1]!=-1:
                return dp[m-1][n-1]
            if s1[m-1]==s2[n-1]:
                dp[m-1][n-1]=solve(s1,s2,m-1,n-1)
                return dp[m-1][n-1]
            left=solve(s1,s2,m-1,n)
            right=solve(s1,s2,m,n-1)
            ans=1+min(left,right)
            dp[m-1][n-1]=ans
            return dp[m-1][n-1]

        dp=[[-1]*(len(word2)+1) for _ in range((len(word1))+1)]
        return solve(word1,word2,len(word1),len(word2))
