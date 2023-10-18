import sys
input = sys.stdin.readline
M,N,L = map(int,input().split())
Guns = sorted(list(map(int, input().split())))
Animals = [list(map(int,input().split())) for _ in range(N)]
# Animals = sorted(filter(lambda e : e[1]<=L, Animals),key=lambda x: x[0])
# print(Guns)
cnt=0
for anim in Animals:
    # print(f"ANIMAL {anim}")
    start = 0
    end = len(Guns)-1
    div = (start+end)//2
    # print(f"{start}({Guns[start]}), {div}({Guns[div]}), {end}({Guns[end]})")
    while(not div in [start,end]):
        if(Guns[div]>anim[0]):
            end = div
        if(Guns[div]<anim[0]):
            start = div
        if(Guns[div] == anim[0]):
            break
        div = (start+end)//2
        # print(f"{start}({Guns[start]}), {div}({Guns[div]}), {end}({Guns[end]})")
    # print(f"div: {div}({Guns[div]})")
    for i in [div,end,start]:
        if abs(Guns[i]-anim[0])+anim[1] <= L:
            cnt+=1
            # print("count")
            break
print(cnt)

  


