import sys
input = sys.stdin.readline
N=int(input())
W=[input().strip() for _ in range(N)]
S=sorted(sorted(set(W)),key=len)
print('\n'.join(S))