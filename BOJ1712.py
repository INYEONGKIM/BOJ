a,b,c=map(int,input().split())
if b>=c:
    print(-1)
else:
    c-=b
    print(a//c+1)
