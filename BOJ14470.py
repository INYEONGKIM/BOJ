a=[]
for _ in range(5):
    a.append(int(input()))
res=0
if a[0]<0:
    res+=abs(a[0])*a[2]+a[3]
    a[0]=0
res+=(a[1]-a[0])*a[4]
print(res)
