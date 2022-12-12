from heapq import*
class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap=[]
        for i in range(len(arr)):
            dist=abs(arr[i]-x)
            if len(max_heap)<k:
                heappush(max_heap,(-dist,arr[i]))
            else:
                if dist < -1*max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap,(-dist,arr[i]))
       
        ans=[]
        while max_heap:
            dis,val=heappop(max_heap)
            ans.append(val)
        return sorted(ans)
        
