#User function Template for python3
class Solution:
    def solve(self, n, p ,a, b, d): 
        graph = [[] for i in range(n+1)]
        isStartingNode = [True]*(n+1)
        for i in range(p):
            graph[a[i]] = [b[i], d[i]]
            isStartingNode[b[i]] = False
        ans = []
        for node in range(1, n+1):
            if isStartingNode[node]:
                currNode = node
                minD = float("inf")
                while graph[currNode]:
                    minD = min(minD, graph[currNode][1])
                    currNode = graph[currNode][0]
                if node != currNode:
                    ans.append([node, currNode, minD])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))


# } Driver Code Ends