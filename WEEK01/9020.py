import sys
sys = sys.stdin.readline

T=int(input())
N=[int(input()) for _ in range(T)]
maxN = max(N)+1
p = [False,False] + [True] * maxN
for i in range(2,maxN):
    if(p[i]):
        for x in range(i*2,maxN,i):
            p[x]=False

for n in N:
    for i in range(n//2,n):
        if(p[i] and p[n-i]):
            print(n-i,i)
            break
