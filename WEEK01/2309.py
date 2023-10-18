import sys
input = sys.stdin.readline
D=sorted([int(input()) for _ in range(9)])
sumFake = sum(D)-100
find = False
for i in range(9):
    if find :break
    for j in range(9):
        if i!=j and D[i]+D[j]==sumFake:
            D.pop(j)
            D.pop(i)
            find=True
            break
print('\n'.join(list(map(str,D))))