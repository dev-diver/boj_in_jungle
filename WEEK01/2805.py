import sys
input = sys.stdin.readline
N,M = map(int,input().split())
T = sorted(list(map(int, input().split())),reverse=True)
find = False

def isEnough(H):
    sum = 0
    for t in T:
        sum+=t-H
        if(sum>=M): 
            return True

start = 0
end = T[0]
div = (start+end)//2
while(not div in [start,end]):
    if isEnough(div):
        start = div
    else:
        end = div
    div = (start+end)//2    
    # print(start, div, end)
print(div)


