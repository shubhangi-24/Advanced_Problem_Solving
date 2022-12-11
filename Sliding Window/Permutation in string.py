def checkInclusion(self, s1: str, s2: str) -> bool:
        map=dict()
        for ch in s1:
            map[ch]=map.get(ch,0)+1
        ws=0
        matched=0
        for we in range(len(s2)):
            curchar=s2[we]
            if curchar in map:
                map[curchar]=map[curchar]-1
                if map[curchar]==0:
                    matched+=1
            if matched==len(map):
                return True
            if we>=len(s1)-1:
                leftchar=s2[ws]
                ws+=1
                if leftchar in map:
                    if map[leftchar]==0:
                        matched-=1
                    map[leftchar]=map[leftchar]+1
        return False
