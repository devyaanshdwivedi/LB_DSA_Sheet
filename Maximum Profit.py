#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        k=K
        n=N
        price=A
        dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        
        for index in range (n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy==1:
                        dp[index][buy][cap]=max((-price[index]+dp[index+1][0][cap],0+dp[index+1][1][cap]))
                        
                    elif buy==0:
                        dp[index][buy][cap]=max((price[index]+dp[index+1][1][cap-1],0+dp[index+1][0][cap]))
        #print(dp)                
        return dp[0][1][k]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends