 def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for we in range(len(nums)):
            if(nums[we] in d and abs(d[nums[we]]-we)<=k):
                return True
            d[nums[we]]=we
        return False
