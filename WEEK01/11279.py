import heapq
import sys
input = sys.stdin.readline
N = int(input())
commands = [int(input()) for _ in range(N)]

text = []
heap = []
for com in commands:
    if com==0:
        ans = heapq.heappop(heap)[1] if len(heap)!=0 else 0
        text.append(str(ans))
    else:
        heapq.heappush(heap,(-com,com))

print('\n'.join(text))