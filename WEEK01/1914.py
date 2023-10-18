N=int(input())
text=[]
def move(n,a,c,b):  #n개의 원판을 a에서 b로 옮기는 함수
    cnt=0
    if n>1:
        cnt+=move(n-1,a,b,c)
    if N <=20 :text.append(f'{a} {c}')
    if n>1:
        cnt+=move(n-1,b,c,a)
    return cnt+1
def move2(n):
    cnt=0
    if n>1:
        cnt+=move2(n-1)*2
    return cnt+1
if N<=20:
    print(move(N,1,3,2))
    print('\n'.join(text))
else:
    print(move2(N))