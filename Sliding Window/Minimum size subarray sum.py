def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start=0
        window_sum=0
        min_len=math.inf
        for window_end in range(len(nums)):
            window_sum+=nums[window_end]
            while window_sum>=target:
                min_len=min(min_len,window_end-window_start+1)
                window_sum-=nums[window_start]
                window_start+=1
        if min_len==math.inf:
            return 0
        else:
            return min_len
        
        
