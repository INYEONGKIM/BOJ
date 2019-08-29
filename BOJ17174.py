n,m=map(int,input().split());r=0
while n>0:
    r+=n;n//=m
print(r)
