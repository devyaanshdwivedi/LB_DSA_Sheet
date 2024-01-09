from typing import List


from typing import List


class Solution:
    
    def determinant(self, matrix):
        det = 0
        if len(matrix) == 1:
            return matrix[0][0]
        
        elif len(matrix) == 2:
            return (matrix[0][0]*matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        
        else:
            for k in range(len(matrix)):
                tempMatrix = []
                for i in range(1, len(matrix)):
                    row = []
                    for j in range(len(matrix)):
                        if j != k :
                            row.append(matrix[i][j])
                    
                    if len(row) > 0:
                        tempMatrix.append(row)
                
                det = det + matrix[0][k] * pow(-1, k) * self.determinant(tempMatrix)
            
            return det
    
    def countSpanningTrees(self, graph : List[List[int]],n : int,m : int) -> int:
        # code here
        # time -- O(n^4)
        # space -- O(n^2)
        
        adj = [[0]*n for i in range(n)]
        
        for a, b in graph:
            adj[a][b] = 1
            adj[b][a] = 1
        
        # laplacian matrix
        degree = [0 for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if adj[i][j] == 1:
                    degree[i] += 1
            
        for i in range(n):
            adj[i][i] = degree[i] 
        
        for i in range(n):
            for j in range(n):
                if i!= j and adj[i][j] == 1:
                    adj[i][j] = -1
        
        # submatrix
        submatrix = [[0]*(n-1) for i in range(n-1)]
        
        for i in range(1, n):
            for j in range(1, n):
                submatrix[i-1][j-1] = adj[i][j]
        
        return int(self.determinant(submatrix))
        



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
        
        a=IntArray().Input(2)
        
        
        graph=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.countSpanningTrees(graph,a[0],a[1])
        
        print(res)
        

# } Driver Code Ends