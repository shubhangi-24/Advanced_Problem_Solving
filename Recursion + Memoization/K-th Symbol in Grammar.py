class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n,k):
            if n==1 or k==1:
                return 0
            prevrow=n-1
            elements=2**(prevrow-1)
            if k>elements:
                return 1-solve(n-1,k-elements)
            else:
                return solve(n-1,k)
        
        return solve(n,k)
