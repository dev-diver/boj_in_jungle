import sys
input = sys.stdin.readline
input()
N=list(map(int,input().split()))
maxN=max(N)+1
p = [0,0]+[1]*(maxN-2)
for i in range(2,maxN):
    if(p[i]==1):
        for x in range(i*2,maxN,i):
            p[x]=0
cnt = 0
for i in N:
    if(p[i]==1): cnt+=1
print(cnt)