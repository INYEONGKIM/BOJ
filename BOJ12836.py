input=__import__('sys').stdin.readline
n,c=map(int,input().split());a=[0]*n;r=""
for _ in range(c):
    q,p,x=map(int,input().split())
    if q==1: a[p-1]+=x
    else: r+=str(sum(a[p-1:x]))+'\n'
print(r,end="")
