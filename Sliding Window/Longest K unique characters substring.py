def longestKSubstr(self, s, k):
        w_start=0
        w_end=0
        maxlen=0
        d={}
        if len(s)<k:
            return -1
        else:
            
            for w_end in range(len(s)):
                curchar=s[w_end]
                d[curchar]=d.get(curchar,0)+1
                while len(d)>k:
                    leftchar=s[w_start]
                    d[leftchar]=d.get(leftchar,0)-1
                    if d[leftchar]==0:
                        d.pop(leftchar)
                    w_start+=1
                if len(d)==k:
                    maxlen=max(maxlen,w_end-w_start+1)
            if maxlen==0:
                return -1
            else:
                return maxlen
