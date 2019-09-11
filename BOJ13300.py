input=__import__('sys').stdin.readline
n,k=map(int,input().split());a=[[0]*6 for _ in range(2)];t=0
for _ in range(n):
    x,y=map(int,input().split())
    a[x][y-1]+=1
for i in range(2):
    for j in a[i]:
        t+=j//k
        if j%k>0: t+=1
print(t)
