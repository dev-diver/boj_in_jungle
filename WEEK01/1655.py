import sys
import heapq
input = sys.stdin.readline
N = int(input())
numbers =  [int(input()) for _ in range(N)]
MAX = 10001
low = [MAX] #낮은 수,  최대힙
high = [MAX] # 큰 수 , 최소힙
result = []
for number in numbers:
    if(len(low)==len(high)):
        heapq.heappush(low,-number)
    else:
        heapq.heappush(high,number)
    if -low[0] > high[0]:
        v = -heapq.heappop(low)
        w = heapq.heappop(high)
        heapq.heappush(high,v)
        heapq.heappush(low,-w)
    result.append(str(-low[0]))
print('\n'.join(result))