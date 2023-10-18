import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
r = []

for i in range(M):
    if B[i] in A:
        r.append("1")
    else:
        r.append("0")
print('\n'.join(r))