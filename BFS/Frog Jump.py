class Solution:
    def canCross(self, stones: List[int]) -> bool:
        destination=stones[len(stones)-1]
        map=dict()
        for stone in stones:
            map[stone]=set()

        map[stones[0]].add(1)
        
        for pos in stones:
            jumps=map[pos]
            for j in jumps:
                new_pos=pos+j
                if new_pos==destination:
                    return True
                if new_pos in map:
                    if j-1>0:
                        map[new_pos].add(j-1)
                    map[new_pos].add(j)
                    map[new_pos].add(j+1)
        return False
