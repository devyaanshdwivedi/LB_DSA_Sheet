import sys
maxint=int(1e9+7)
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        m = [[0 for x in range(N)] for x in range(N)]
 
    # m[i, j] = Minimum number of scalar 
    # multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = 
    # A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
        for i in range(1, N):
            m[i][i] = 0
 
    # L is chain length.
        for L in range(2, N):
            for i in range(1, N-L + 1):
                j = i + L-1
                m[i][j] = maxint
                for k in range(i, j):
 
                # q = cost / scalar multiplications
                    q = m[i][k] + m[k + 1][j] + arr[i-1]*arr[k]*arr[j]
                    if q < m[i][j]:
                        m[i][j] = q
 
        return m[1][N-1]