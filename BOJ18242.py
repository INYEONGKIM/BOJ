n,m=map(int,__import__('sys').stdin.readline().strip().split())
a=[__import__('sys').stdin.readline().strip() for _ in range(n)]
f=False;lrs=-1;idx=-1
for x in a:
    if f: break
    cnt=x.count('#')
    if cnt>2:
        lrs=x.index('#')
    elif cnt==1:
        idx=x.index('#')
        f=True
if f:
    if idx is not lrs:
        print('LEFT')
    else:
        print('RIGHT')
else:
    lf=False;lrs=-1
    for i in range(m):
        if f: break
        cnt=0
        for j in range(n):
            if a[j][i]=='#':
                if not lf:
                    lf=True
                    lrs=j
                cnt+=1;idx=j
        if cnt==1:
            f=True
            if idx!=lrs: print('UP')
            else: print('DOWN')
