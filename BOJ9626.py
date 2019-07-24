x,y=map(int,input().split());u,l,r,d=map(int,input().split())
s=[];res="";f=['#','.'];fidx=0
for _ in range(x):
    s.append(input())
for i in range(u+d+x):
    if i%2==0: fidx=0
    else: fidx=1
    if i<u or i>=u+x:
        for j in range(l+r+y):
            res+=f[fidx%2]
            fidx+=1
    else:
        for j in range(l):
            res+=f[fidx%2]
            fidx+=1
        res+=s[i-u]
        fidx+=len(s[i-u])
        for j in range(r):
            res+=f[fidx%2]
            fidx+=1
    res+='\n'
print(res,end="")
