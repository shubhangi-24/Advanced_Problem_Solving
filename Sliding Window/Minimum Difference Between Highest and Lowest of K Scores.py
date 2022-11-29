def minimumDifference(self, nums: List[int], k: int) -> int:
        w_start=0
        w_end=0
        nums.sort()
        diff=math.inf
        while w_end<len(nums):
            if w_end-w_start+1<k:
                w_end+=1
            else:
                
                diff=min(diff,nums[w_end]-nums[w_start])
                w_start+=1
                w_end+=1
        return diff
            
