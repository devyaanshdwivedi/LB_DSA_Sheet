#User function Template for python3

from heapq import heappush, heappop
class Solution:
    def smallestRange(self, arr, n, k):
        # code here
        # print the smallest range in a new line
        hq = []
        mx = 0
        for i in range(k):
            heappush(hq, (arr[i][0], i, 0))
            mx = max(mx, arr[i][0])
        rang = float('inf')
        while len(hq) >= k:
            mi, row, col = heappop(hq)
            r = mx - mi
            if r < rang:
                rang = r
                ans = [mi, mx]
            if col + 1 < n:
                mx = max(mx, arr[row][col + 1])
                heappush(hq, (arr[row ][col + 1], row, col + 1))
        return ans