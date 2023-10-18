import sys
input = sys.stdin.readline
N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]

def isBase(paper,color):
    l=len(paper)
    first=paper[0][0]
    if(l==1): 
        color[first]+=1
        return True
    for i in range(l):
        for j in range(l):
            if paper[i][j]!=first:
                return False
    color[first]+=1
    return True
    
def divide(paper,color):
    if isBase(paper,color): 
        return
    half = len(paper)//2
    divide([line[:half] for line in paper[:half]],color)
    divide([line[:half] for line in paper[half:]],color)
    divide([line[half:] for line in paper[:half]],color)
    divide([line[half:] for line in paper[half:]],color)
color = [0,0]
divide(P,color)
print(*color)