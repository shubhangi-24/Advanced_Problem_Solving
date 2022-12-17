def frequencySort(self, s: str) -> str:
        map=dict()
        for ch in s:
            map[ch]=map.get(ch,0)+1
        max_heap=[]
        for key,value in map.items():
            heappush(max_heap,(-value,key))
        ans=[]
        while max_heap:
            value,key=heappop(max_heap)
            freq=-value
            for i in range(freq):
                ans.append(key)
        return ''.join(ans)
