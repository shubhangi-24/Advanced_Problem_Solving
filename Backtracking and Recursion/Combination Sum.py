class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        powerset=[]
        def solve(subset,powerset,i,s,target):
            if i==len(candidates) and s==target:
                powerset.append(subset.copy())
                return
            if s>target:
                return
            if i==len(candidates):
                return
            if s==target:
                powerset.append(subset.copy())
                return
            else:
                # include
                if candidates[i]<=target:
                    subset.append(candidates[i])
                    s+=candidates[i]
                    solve(subset,powerset,i,s,target)
                    subset.pop()
                    s-=candidates[i]

                #ignore
                solve(subset,powerset,i+1,s,target)

        subset=[]
        solve(subset,powerset,0,0,target)
        return powerset
