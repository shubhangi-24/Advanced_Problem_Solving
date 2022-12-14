def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for i in range(len(stones)):
            heappush(max_heap,-stones[i])
        while len(max_heap)>1:
            x=heappop(max_heap)
            y=heappop(max_heap)
            diff=y-x
            if diff!=0:
                heappush(max_heap,-diff)
        return -max_heap[0] if max_heap else 0
