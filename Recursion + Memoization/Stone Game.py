class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def solve(piles,left,right):
            if left>right:
                return 0
            if dp[left][right]!=-1:
                return dp[left][right]
            l=piles[left]-solve(piles,left+1,right)
            r=piles[right]-solve(piles,left,right-1)
            ans=max(l,r)
            dp[left][right]=ans
            return dp[left][right]
    
        dp=[[-1]*len(piles) for _ in range(len(piles))]
        score=solve(piles,0,len(piles)-1)
        if score>0:
            return True
        else:
            return False
