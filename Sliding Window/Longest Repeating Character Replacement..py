def characterReplacement(self, s: str, k: int) -> int:
        w_start=0
        w_end=0
        d={}
        maxlen=0
        mfec=0
        for w_end in range(len(s)):
            currchar=s[w_end]
            d[currchar]=d.get(currchar,0)+1
            mfec=max(mfec,d.get(currchar))
            if (w_end-w_start+1)-mfec>k:
                leftchar=s[w_start]
                d[leftchar]=d.get(leftchar)-1
                w_start+=1
            maxlen=max(maxlen,w_end-w_start+1)
        return maxlen
