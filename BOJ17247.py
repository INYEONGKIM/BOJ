x,y=map(int,input().split());l=[]
for i in range(x):
    l.append([int(j) for j in input().split()])
a,b,c,d,f=0,0,0,0,False
for i in range(x):
    for j in range(y):
        if l[i][j]==1:
            if not f:
                a=i;b=j;f=True
            else:
                c=i;d=j
print(abs(a-c)+abs(b-d))
