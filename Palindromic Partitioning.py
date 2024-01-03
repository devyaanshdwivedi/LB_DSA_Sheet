#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        n=len(string)
        dp1=[[0]*n for i in range(n)]
        dp2=[[0]*n for i in range(n)]
        for i in range(n-1):
            dp1[i][i]=1
            if string[i]==string[i+1]:
                dp1[i][i+1]=1
        dp1[n-1][n-1]=1
        for l in range(2,n):
            for i in range(n-l):
                j=i+l
                if string[i]==string[j] and dp1[i+1][j-1]:
                    dp1[i][j]=1
        for i in range(n):
            if not dp1[i][n-1]:
                dp2[n-1][i]=1000
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                if dp1[j][i]:
                    dp2[i][j]=min(1+dp2[i+1][i+1],dp2[i+1][j])
                else:
                    dp2[i][j]=dp2[i+1][j]
        return dp2[0][0]
        # code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends