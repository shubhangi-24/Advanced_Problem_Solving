def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        prev=intervals[0]
        merged_intervals=[]
        for i in range(1,len(intervals)):
            current=intervals[i]
            if current[0]<=prev[1]:
                prev[1]=max(current[1],prev[1])
            else:
                merged_intervals.append(prev)
                prev=current
        merged_intervals.append(prev)
        return merged_intervals
