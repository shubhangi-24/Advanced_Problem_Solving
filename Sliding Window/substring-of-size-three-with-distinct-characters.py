 def countGoodSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            c=set(s[i:i+3])
            if len(c)==3:
                ans+=1
        return ans
        
