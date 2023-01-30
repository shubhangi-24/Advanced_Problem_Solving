class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        powerset=[]
        nums.sort()
        def solve(nums,subset,powerset,i):
            if i==len(nums):
                powerset.append(subset.copy())
                return

            #include
            subset.append(nums[i])
            solve(nums,subset,powerset,i+1)
            subset.pop()

            #ignore
            while(i<len(nums)-1 and nums[i]==nums[i+1]):
                i+=1
            solve(nums,subset,powerset,i+1)

        subset=[]
        solve(nums,subset,powerset,0)
        return powerset
