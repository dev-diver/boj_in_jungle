from collections import deque
N,K=map(int,input().split())
deq = deque([str(i+1) for i in range(N)],N)
cnt=0
result = []
while(len(deq)):
    cnt+=1
    val = deq.popleft()
    if cnt%K!=0:
        deq.append(val)
    else:
        result.append(val)
text=", ".join(result)
print(f"<{text}>")