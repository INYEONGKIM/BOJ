n=int(input());a=[int(i) for i in input().split()];x=int(input());cnt=0
for i in a:
    if x==i: cnt+=1
print(cnt)
