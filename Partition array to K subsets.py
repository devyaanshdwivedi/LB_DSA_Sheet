#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        
        if k==1:
            return True
        
        n = len(a)
        sm = sum(a)
        if sm%k!=0:
            return False
        
        partSum = sm // k
        visited = set()
        def dfs(partSum, tempSum, index, visited, count):
            
            if tempSum==partSum:
                #print(tempSum, index, count)
                if count ==k-1:
                    return True
                
                return dfs(partSum, 0, 0, visited, count+1)
                
            
            for i in range(index, len(a)):
                if i in visited:
                    continue
                
                if tempSum + a[i]<=partSum:
                    visited.add(i)
                    if dfs(partSum, tempSum + a[i], i+1, visited, count):
                        return True
                    
                    
                    visited.remove(i)
                    #return x
            
            return False
        return dfs(partSum, 0, 0, visited, 0)
                
                
                
                
                
                

#{ 
 # Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends