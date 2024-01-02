#User function Template for python3

class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        dic=set()
        for el in dict:
            dic.add(el)
        ans=[]
        
        def find(s,dic,i,avail,par_ans):
            if i>=len(s):
                if not par_ans:
                    ans.append(' '.join(avail))
                return
            par_ans+=s[i]
            if par_ans in dic:
                avail.append(par_ans)
                find(s,dic,i+1,avail,'')
                avail.pop()
            find(s,dic,i+1,avail,par_ans)
                
        find(s,dic,0,[],'')
        return ans