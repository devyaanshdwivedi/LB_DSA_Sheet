from typing import List


class Solution:
    def findMaxValue(self, n : int, mat : List[List[int]]) -> int:
        # code here
        
        # brute force O(n^4) O(1)
        # 4 loops -> check everything -> find difference -> give max diff
        
        
        # Optimal O(n^2) O(n^2)
        precompute=[[0]*n for _ in range(n)]
        
        precompute[n-1][n-1]=mat[n-1][n-1]
        
        maxval=mat[n-1][n-1]


        # last row
        for i in range(n-2, -1, -1):
            if mat[n-1][i]>maxval:
                maxval=mat[n-1][i]
            precompute[n-1][i]=maxval
            
            
            
        maxval=mat[n-1][n-1]
        
        # Last col
        for i in range(n-2, -1,-1):
            if mat[i][n-1]>maxval:
                maxval=mat[i][n-1]
                
            precompute[i][n-1]=maxval
            
            
 
        maxval=float('-inf')

        # Remaining cells
        
        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                
                if precompute[i+1][j+1]-mat[i][j]>maxval:
                    maxval=precompute[i+1][j+1]-mat[i][j]
                    
                precompute[i][j]=max(mat[i][j], precompute[i+1][j], precompute[i][j+1])
                
    
        return maxval            
