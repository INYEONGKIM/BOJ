c=0;a=[];n=int(input())
for _ in range(n):
    v,p=map(int,input().split())
    a.append(v)
a.sort(reverse=True);k=a[4]
for i in range(5,n):
    if k==a[i]: c+=1
    else: break
print(c)
