 def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        w_start=0
        w_prod=1
        ans=0
        for w_end in range(len(nums)):
            w_prod*=nums[w_end]
            if w_prod<k:
                ans+=w_end-w_start+1
            else:
                while w_start<=w_end and w_prod>=k:
                    w_prod=w_prod/nums[w_start]
                    w_start+=1
                ans+=w_end-w_start+1
        return ans
