input=__import__('sys').stdin.readline
l=[];n=int(input())
for _ in range(n):
    t=[]
    for _ in range(5): t.append(list(input()))
    l.append(t)
d=36;fx=0;fy=0
for i in range(n-1):
    for j in range(i+1,n):
        c=0
        for k in range(5):
            for v in range(7):
                if l[i][k][v]!=l[j][k][v]: c+=1
                if d<c: continue
        if d>c: d=c;fx=i+1;fy=j+1
print(fx,fy)
