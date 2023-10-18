S=[*input()]

ans = 0
mult = 1
stack = []
for s in S:
    if s =="(":
        mult*=2
        stack.append(s)
    if s =="[":
        mult*=3
        stack.append(s)
    if s ==")":
        if(not stack or stack[-1]!="("):
            ans=0
            break
        stack.pop()
        ans+=mult
        mult /=2
    if s =="]":
        if(not stack or stack[-1]!="["):
            ans=0
            break
        stack.pop()
        ans+=mult
        mult /=3
print(int(ans))