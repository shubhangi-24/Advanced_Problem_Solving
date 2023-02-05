class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def track(seq,current):
            if not seq:
                res.append(current)
                return res
            for letter in d[seq[0]]:
                track(seq[1:],current+letter)
                
        track(digits,"")
        return res
        
        
