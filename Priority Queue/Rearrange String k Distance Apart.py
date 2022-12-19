from heapq import *
from collections import deque

def ReorganizeStringKDistanceApart(s,k):
        map={}
        for ch in s:
            map[ch]=map.get(ch,0)+1
        maxheap=[]
        for key,value in map.items():
            heappush(maxheap,(-value,key))
        queue=deque()
        res=[]
        while maxheap:
            value,key=heappop(maxheap)
            freq=-value
            res.append(key)
            freq-=1
            queue.append((key,freq))
            if len(queue)==k:
                ch,val=queue.popleft()
                if val>0:
                    heappush(maxheap,(-val,ch))
        if len(res)==len(s):
            return ''.join(res)
        else:
            return ""
        
if __name__ == '__main__':
	s = "aabbcc"
	k = 3
	ans = ReorganizeStringKDistanceApart(s, k)
	print(ans)
