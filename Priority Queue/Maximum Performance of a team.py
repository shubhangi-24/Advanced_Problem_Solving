def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        teams=[]
        for i in range(n):
            teams.append([speed[i],efficiency[i]])
        maxefficiency=0
        total_speed=0
        teams.sort(key=lambda x:x[1])
        min_heap=[]
        for i in range(n-1,-1,-1):
            total_speed+=teams[i][0]
            heappush(min_heap,teams[i][0])
            maxefficiency=max(maxefficiency,total_speed*teams[i][1])
            if len(min_heap)==k:
                total_speed-=heappop(min_heap)
        return maxefficiency%((10**9)+7)
