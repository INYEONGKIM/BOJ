input=__import__('sys').stdin.readline
n,q=map(int,input().split());l=[False]*n;c=0
for _ in range(q):
    s,i=map(int,input().split());s-=1
    while s<n:
        l[s]=True
        s+=i
for i in l:
    if not i: c+=1
print(c)
