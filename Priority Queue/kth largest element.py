def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr=[int(val) for val in nums]
        min_heap=[]
        for i in range(len(arr)):
            heappush(min_heap,arr[i])
            if len(min_heap)==k+1:
                heappop(min_heap)
        return str(min_heap[0])
