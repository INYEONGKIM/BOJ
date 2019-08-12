r=0;m=0
for _ in range(4):
    o,i=map(int,input().split())
    r+=i-o
    if r>m: m=r
print(m)
