trips.sort(key=lambda x: x[1])
        minheap=[]
        for trip in trips:
            c=trip[0]
            start=trip[1]
            end=trip[2]
            while minheap and minheap[0][0]<=start:
                vacant,cap=heappop(minheap)
                capacity+=vacant
            if c>capacity:
                return False
            else:
                capacity-=trip[0]
                heappush(minheap,(end,c))
        return True
