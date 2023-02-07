class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        powerset=[]
        nums=list(range(1,10))
        def solve(subset,powerset,i,s,target):
            if i==len(nums) and s==target and len(subset)==k:
                powerset.append(subset.copy())
                return
            if s>target:
                return
            if i==len(nums):
                return
            if s==target and len(subset)==k:
                powerset.append(subset.copy())
                return
            else:
                # include
                if nums[i]<=target:
                    subset.append(nums[i])
                    s+=nums[i]
                    solve(subset,powerset,i+1,s,target)
                    subset.pop()
                    s-=nums[i]

                #ignore
                solve(subset,powerset,i+1,s,target)

        subset=[]
        solve(subset,powerset,0,0,n)
        return powerset
