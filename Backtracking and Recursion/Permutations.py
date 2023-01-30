class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(nums,l,r):
            if l==r:
                ans.append(nums.copy())
                return
            else:
                for i in range(l,r+1):
                    nums[i],nums[l]=nums[l],nums[i]
                    solve(nums,l+1,r)
                    nums[l],nums[i]=nums[i],nums[l]
        solve(nums,0,len(nums)-1)
        return ans
