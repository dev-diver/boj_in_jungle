import sys
import heapq
input = sys.stdin.readline
N = int(input())
P = [tuple(sorted(map(int,input().split()))) for _ in range(N)]
L = int(input())
# 튜플의 첫번째 요소가 정렬의 기준
P = sorted(P,key=lambda x:(x[1],x[0]))
# print(P)
maxP = 0
heap=[]
for road in P:
    # print(road[1]-L,"~",road[1])
    if(road[1]-road[0]>L): continue
    heapq.heappush(heap,road)
    # print(heap)
    while(heap):
        if(heap[0][0]<road[1]-L):
            v = heapq.heappop(heap)
            # print(v)
        else:
            break
    # print(heap)
    cnt = len(heap)
    # print(cnt)
    maxP = max(maxP,cnt)

print(maxP)