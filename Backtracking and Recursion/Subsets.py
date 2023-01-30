class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset=[]
        def solve(nums,subset,powerset,i):
            if i==len(nums):
                powerset.append(subset.copy())
                return

            #include
            subset.append(nums[i])
            solve(nums,subset,powerset,i+1)
            subset.pop()

            #ignore
            solve(nums,subset,powerset,i+1)
        
        subset=[]
        solve(nums,subset,powerset,0)
        return powerset

       

         
