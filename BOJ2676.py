k=int(input())
res=""
for i in range(k):
    n,m = map(int, input().split())
    res+=(str(1+m*(n-m))+"\n")
print(res,end="")
