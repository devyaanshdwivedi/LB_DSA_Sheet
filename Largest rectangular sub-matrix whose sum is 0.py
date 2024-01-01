from typing import List


from typing import List


class Solution:
    def max_sub_sum(self,arr):
        n=len(arr)
        prefix_sum={0:-1}
        _sum=0
        s,e=0,0
        max_len=-float("inf")
        curr_len=0
        for i in range(n):
            _sum+=arr[i]
            if _sum in prefix_sum:
                curr_len=i-prefix_sum[_sum]
                if curr_len>max_len:
                    max_len=curr_len
                    e=i
                    s=prefix_sum[_sum]+1
            else:
                prefix_sum[_sum]=i
        return (s,e,max_len)
        
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        # code here
        n,m=len(a),len(a[0])
        r1,r2,c1,c2,max_area=None,None,None,None,-float("inf")
        for i in range(m):
            arr=[0]*n
            for j in range(i,m):
                for k in range(n):
                    arr[k]+=a[k][j]
                s,e,length=self.max_sub_sum(arr)
                area=(e-s+1)*(j-i+1)
                if length>0 and area>max_area:
                    max_area=area
                    r1,r2,c1,c2=s,e,i,j
        result=[]
        for i in range(r1,r2+1):
            row_i=[]
            for j in range(c1,c2+1):
                row_i.append(a[i][j])
            result.append(row_i)
        return result

