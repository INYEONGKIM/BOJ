input=__import__('sys').stdin.readline
n,m=map(int,input().split());a=[];gu=0;mgu=-1
for _ in range(n):
    tgu=0
    t=input().split()
    for i in t:
        for x in i:
            if x=='9': gu+=1;tgu+=1
    if tgu>mgu: mgu=tgu
    a.append(t)
for i in range(m):
    tgu=0
    for j in range(n):
        for x in a[j][i]:
            if x=='9': tgu+=1
    if tgu>mgu: mgu=tgu
print(gu-mgu)
