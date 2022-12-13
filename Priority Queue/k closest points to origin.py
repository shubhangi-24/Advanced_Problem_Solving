def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        for i in range(len(points)):
            dist=points[i][0]*points[i][0]+points[i][1]*points[i][1]
            heappush(max_heap,(-dist,points[i][0],points[i][1]))
            if len(max_heap)==k+1:
                heappop(max_heap)
        ans=[]
        while max_heap:
            d,x,y=heappop(max_heap)
            ans.append([x,y])
        return ans
