import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N=int(input())
M = [list(map(int,input().split())) for _ in range(N)]
#1<rain<2
def count_safe(rain):
    #WET
    W =[[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if(M[row][col]<=rain):
                W[row][col] = 1
    # print(f"WET {rain} \n {W}")
    V =[[0]*N for _ in range(N)]
    cnt=0
    for row in range(N):
        for col in range(N):
            result=makezone(row,col,V,W)
            # if(result): print(row, col)
            cnt+=result
    return cnt

def makezone(i,j,V,W):
    l=len(V)
    if i>=l or j>=l or i<0 or j<0 or V[i][j]==1 or W[i][j]==1: return 0
    V[i][j] = 1
    makezone(i-1,j,V,W)
    makezone(i+1,j,V,W)
    makezone(i,j-1,V,W)
    makezone(i,j+1,V,W)
    return 1

maxRain = max([max(arr) for arr in M])
maxSafe = 0
for rain in range(0,maxRain):
    maxSafe = max(maxSafe, count_safe(rain))

print(maxSafe)