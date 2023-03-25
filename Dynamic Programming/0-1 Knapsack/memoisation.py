def knapSack(self,W, wt, val, n):
        dp=[[-1 for _ in range(W+1)] for _ in range(n+1)]
        if n==0 or W==0:
            return 0
        if dp[n][W]!=-1:
            return dp[n][W]
        if wt[n-1]<=W:
            dp[n][W]=max(val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1),self.knapSack(W,wt,val,n-1))
            return dp[n][W]
        elif wt[n-1]>W:
            dp[n][W]=self.knapSack(W,wt,val,n-1)
            return dp[n][W]
