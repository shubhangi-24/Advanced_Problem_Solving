def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=dict()
        for i in nums:
            map[i]=map.get(i,0)+1
        min_heap=[]
        ans=[]
        for key,value in map.items():
            heappush(min_heap,(value,key))
            if len(min_heap)==k+1:
                val,key=heappop(min_heap)
        while min_heap:
            val,key=heappop(min_heap)
            ans.append(key)
        return ans
