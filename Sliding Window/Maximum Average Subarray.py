def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start=0
        window_sum=0
        window_avg=-math.inf
        for window_end in range(len(nums)):
            window_sum+=nums[window_end]
            if window_end>=k-1:
                wavg=(window_sum/k)
                window_avg=max(wavg,window_avg)
                window_sum-=nums[window_start]
                window_start+=1
                
        return window_avg
