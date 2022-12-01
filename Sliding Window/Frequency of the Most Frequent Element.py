def maxFrequency(self, nums: List[int], k: int) -> int:
        w_start=0
        w_end=0
        ans=0
        cur_sum=0
        nums.sort()
        while w_end<len(nums):
            cur_sum+=nums[w_end]
            
            while nums[w_end]*(w_end-w_start+1)>cur_sum+k:
                cur_sum-=nums[w_start]
                w_start+=1
                
            ans=max(ans,w_end-w_start+1)
            w_end+=1
        return ans
      
