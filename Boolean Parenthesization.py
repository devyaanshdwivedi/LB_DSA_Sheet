#User function Template for python3


class Solution:
    def countWays(self, N, S):
        
        
        
      
        
        def memoized3dcountnumberofways(s,i,j,isTrue):

            if i>j:
                return False
            
            if i==j:
                if isTrue == True:
                    return int(s[i] == 'T')
                else:
                    return int(s[i] == 'F')
                    
            if dp[i][j][int(isTrue)]!= -1:
                return int(dp[i][j][int(isTrue)])
        
            ans = 0
            for k in range(i+1,j,2):
                rt= memoized3dcountnumberofways(s,k+1,j,True)
                rf= memoized3dcountnumberofways(s,k+1,j,False)
                lt= memoized3dcountnumberofways(s,i,k-1,True)
                lf= memoized3dcountnumberofways(s,i,k-1,False)
        
        
                if s[k] == '^':
                    if isTrue == True:
                        ans += (rt * lf + rf * lt)
                    else:
                        ans+= (rf * lf + rt * lt)
                elif s[k] == '&':
                    if isTrue == True:
                        ans+= rt * lt
                    else:
                        ans+= (rf * lf + rt * lf + rf * lt)
                elif s[k] == '|':
                    if isTrue == True:
                        ans += (rt * lt + rf * lt + rt * lf)
                    else:
                        ans += rf * lf 
            dp[i][j][int(isTrue)] = ans
            return ans%1003







        dp =  [[[-1 for _ in range(2)] for _ in range(201)] for _ in range(201)]



        return memoized3dcountnumberofways(S, 0, len(S) - 1, True)
        