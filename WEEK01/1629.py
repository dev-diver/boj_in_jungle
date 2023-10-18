import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
A,B,C = map(int,input().split())

def mod(A,B,C):
    if(B==1): return A%C
    half = B//2
    halfmod = mod(A,half,C)
    halfC = (halfmod*halfmod)%C
    if(B%2==0): # 짝수면
        return halfC
    else:
        return (halfC*(A%C))%C

print(mod(A,B,C))