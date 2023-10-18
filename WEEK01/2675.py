import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    R, S = input().split()
    P = ''.join([C*int(R) for C in S])
    print(P)