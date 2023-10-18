import sys
input = sys.stdin.readline
N=int(input())
commands = [input().split() for _ in range(N)]

MAX = 10000
class Stack:

    def __init__(self,size):
        self.arr = [None]*size
        self.last = 0
        self.length = 0
        return
    
    def push(self, val):
        self.arr[self.last]=val
        self.last+=1
        self.length+=1
        return
    
    def pop(self):
        if(self.empty()):
            return -1
        val = self.top()
        self.last-=1
        self.length-=1
        return val
    
    def size(self):
        if(self.empty()):
            return 0
        return self.length
    
    def empty(self):
        return 1 if self.length==0 else 0
    
    def top(self):
        if self.length <= 0: return -1
        return self.arr[self.last-1]
    
stack = Stack(MAX)
result = []
for com in commands:
    c = com[0]
    val = com[1] if len(com) > 1 else None
    if c=='push':
        stack.push(val)
    elif c =='pop':   
        result.append(stack.pop())
    elif c =='size': 
        result.append(stack.size())
    elif c =='empty':   
        result.append(stack.empty())
    elif c =='top':  
        result.append(stack.top())

print('\n'.join(map(str,result)))