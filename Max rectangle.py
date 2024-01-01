#User function Template for python3


class Solution:
    def findarea(self,array,n):
        stack=[]
        area=0
        for i in range(n+1):
            while stack and (i==n or array[stack[-1]]>=array[i]):
                height=array[stack.pop()]
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                area=max(area,width*height)
            stack.append(i)
        return area
    def maxArea(self,M, n, m):
        histogram=[0 for i in range(m)]
        maxi=0
        for i in range(n):
            for j in range(m):
                if M[i][j]==0:
                    histogram[j]=0
                else:
                    histogram[j]+=1
            maxi=max(maxi,self.findarea(histogram,m))
        return maxi
        # code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends