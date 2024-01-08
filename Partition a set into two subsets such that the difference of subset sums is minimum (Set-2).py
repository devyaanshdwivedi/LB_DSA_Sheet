from typing import List




        # code here
        
from typing import List

class Solution:
    def minDifference(self, n : int, a : List[int]) -> List[List[int]]:
        # code here
        
        
        def md(i, s1, s2, ans, l1, l2):
            
            if n%2 == 0 and (l1>n//2 or l2>n//2):
                return
            elif n%2 == 1 and (l1>(n//2)+1 or l2>(n//2)+1):
                return
            
            
            if i == n:
                if abs(s1-s2) < ans[1][0]-ans[0][0]:
                    ans[:] = sorted([[s1], [s2]])
                return
            
            
            md(i+1, s1+a[i], s2, ans, l1+1, l2)
            md(i+1, s1, s2+a[i], ans, l1, l2+1)
            
        n = len(a)
        ans = [[min(a)], [max(a)]]
        md(0, 0, 0, ans, 0, 0)
        return ans



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minDifference(n, arr)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends