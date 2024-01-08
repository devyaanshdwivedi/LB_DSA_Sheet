
from typing import List


class Solution:
    def overlap(self, n : int, intervals : List[List[int]]) -> int:
        times = []
        for interval in intervals:
            times.append((interval[0],"start"))
            times.append((interval[1],"end"))
        times = sorted(times,key = lambda x: (x[0], 0 if x[1] == 'start' else 1))
        count = 0
        max_count = 0
        for time in times:
            if time[1] == "start":
                count += 1
            if time[1] == "end":
                count -= 1
            max_count = max(max_count,count)
        return max_count
                
        

