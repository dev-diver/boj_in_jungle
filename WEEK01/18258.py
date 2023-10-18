import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
commands = [input().split() for _ in range(N)]
MAX = 2000001
class Que:
    def __init__(self,size):
        self.que = deque([],size)
        self.length = 0

    def push(self,val):
        self.que.append(val)
    
    def pop(self):
        if(self.empty()):
            return -1
        val = self.que.popleft()
        return val
    
    def size(self):
        return len(self.que)
    
    def empty(self):
        return 1 if not len(self.que) else 0
    
    def front(self):
        return self.que[0] if not self.empty() else -1
    
    def back(self):
        return self.que[self.size()-1] if not self.empty() else -1

que = Que(MAX)
text = []
for com in commands:
    c = com[0]
    val = com[1] if len(com)>=2 else None

    if c=='push':
        que.push(val)
    elif c=='pop':
        text.append(que.pop())
    elif c=='size':
        text.append(que.size())
    elif c=='empty':
        text.append(que.empty())
    elif c=='front':
        text.append(que.front())
    elif c=='back':
        text.append(que.back())

print('\n'.join(map(str,text)))