def reorganizeString(self, s: str) -> str:
        map=dict()
        for ch in s:
            map[ch]=map.get(ch,0)+1
        maxheap=[]
        for key,value in map.items():
            heappush(maxheap,(-value,key))
        ans=[]
        while len(maxheap)>=2:
            val1,first=heappop(maxheap)
            val2,second=heappop(maxheap)
            ans.append(first)
            ans.append(second)
            val1+=1
            val2+=1
            if -val1>0:
                heappush(maxheap,(val1,first))
            if -val2>0:
                heappush(maxheap,(val2,second))
        if len(maxheap)==0:
            return ''.join(ans)
        else:
            val,key=heappop(maxheap)
            freq= -val
            if freq==1:
                ans.append(key)
                return ''.join(ans)
            else:
                return ""
