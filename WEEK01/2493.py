import sys
input = sys.stdin.readline
N=int(input())
T= [*map(int,input().split())]

MAX=int(1e9)
arr=[]
arr.append((MAX,-1)) #높이, 인덱스
def stackTree(stack: list, myT :tuple):
    while(stack[-1][0]<myT[0]): 
        stack.pop()
    stack.append(myT)

ans=[]
for i,t in enumerate(T):
    myT = (t,i)
    for k in range(len(arr)-1,-1,-1):
        if(arr[k][0]>myT[0]):
            ans.append(str(arr[k][1]+1))
            break
    stackTree(arr,myT)
    
print(' '.join(ans))
