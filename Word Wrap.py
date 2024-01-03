#User function Template for python3

class Solution:
    def solveWordWrap(self, nums, k):
        #Code here
#         def solveWordWrap(self, arr, k):

 #Code here
        arr=nums
        n=len(arr)
        
        dp=[0]*n
        
        dp[n-1]=0 # Last line is not considered for total sum
        
         
        
        for i in range(n-2,-1,-1):
        
           #  add word:arr[i] in new line 
        
            dp[i]=dp[i+1]+(k-arr[i])**2
        
            l=arr[i]
        
             
        
           # check for possiblity of merging two words in a single line 
        
            for j in range(i+1,n):
        
                l=l+arr[j]+1 # 1: represents the space between two words in a line
        
                if l>k: break
        
                if j==n-1: dp[i]=0 # it means we reached end and we have merged words in last line.
        
                else: dp[i]=min(dp[i],dp[j+1]+(k-l)**2)
        
                 
        
        return dp[0] # return the minimum cost to place all words in lines of k width




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends