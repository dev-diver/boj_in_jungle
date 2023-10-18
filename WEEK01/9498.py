import sys
input = sys.stdin.readline
s = int(input())
result = ''
if 90<=s:
    result = 'A'
elif 80<=s:
    result = 'B'
elif 70<=s:
    result = 'C'
elif 60<=s:
    result = 'D'
else:
    result = 'F'
print(result)