n=int(input())
a=100;b=100
for _ in range(n):
    x,y=map(int,input().split())
    if x-y>0:
        b-=x
    elif x-y<0:
        a-=y
print(a,b,sep="\n")
