import sys
input = sys.stdin.readline
N,B = map(int,input().split())
M = [list(map(int,input().split())) for _ in range(N)]

def pMatrix(A,B):
    size = len(A)
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = sum([A[i][k]*B[k][j] for k in range(size)])%1000
    return C

def expMatrix(M,n):
    if n==1: 
        M = [[e%1000 for e in row] for row in M]
        return M
    half = n//2
    halfM = expMatrix(M,half)
    halfMCompound = pMatrix(halfM,halfM)
    if(n%2==0):  # 짝수면
        return halfMCompound
    else:
        return pMatrix(halfMCompound,M)

result = expMatrix(M,B)
print("\n".join([" ".join(list(map(str,row))) for row in result]))