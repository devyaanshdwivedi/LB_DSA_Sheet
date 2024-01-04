#User function Template for python3

class TrieNode:
     def __init__(self):
        self.children = {}
        self.freq = 0
class Solution:
    def insert(self, root, st):
        for i in range(len(st)):
            c = st[i]
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
            root.freq += 1
    def get_prefix(self, root, st):
        pref = ""
        for i in range(len(st)):
            c = st[i]
            if root.freq == 1:
                break
            pref += c
            root = root.children[c]
        return pref 

    def findPrefixes(self, arr, n):
        root = TrieNode()
        for word in arr:
            self.insert(root, word)
        ans = []
        for word in arr:
            ans.append(self.get_prefix(root, word))
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends